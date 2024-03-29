import rawpy
import imageio
from os import listdir, path, walk, remove
from sys import exit
from multiprocessing import Pool
from argparse import ArgumentParser, BooleanOptionalAction


parser = ArgumentParser(description='Set configurations to convert RAW images to JPEG')
parser.add_argument('-d', '--directory', dest='directory', type=str, nargs=1, help='Folderpath of where your photos are stored')
parser.add_argument('-r', '--remove', dest='remove_old', default=False, action=BooleanOptionalAction, help='Removes RAW files once JPEG images are made.')
parser.add_argument('-o', '--overwrite', dest='overwrite', default=False, action=BooleanOptionalAction, help='Overwrites image files if they already exist')
args = parser.parse_args()

class RawToJpeg():
    def __init__(self, image_folder, delete_old=False, replace=False):
        self.delete_old = delete_old
        self.replace = replace

        if self.delete_old:
            print('\nWARNING: the program is currently configured to delete old images. Are you sure?')
            confirm = input('Continue? (y/n): ')
            if confirm != 'y':
                exit('\Conversion cancelled.\n')
    
        self.image_folder = image_folder
        self.init_size = self.get_folder_stats(self.image_folder)

        self.extensions = ('.CR2', '.ARW', '.NEF', '.nef', '.cr2', '.arw', '.DNG', '.dng')

        try:
            photo_files = []

            for directory, _, files in walk(self.image_folder):
                for file in files:
                    filepath = path.join(directory, file)

                    if file.endswith(self.extensions):
                        # self.convert_image(photo_path=filepath)
                        photo_files.append(filepath)

                    # delete the annoying XML files
                    elif file.endswith('.xml') and self.delete_old:
                        remove(filepath)

            print(f'Converting {len(photo_files)} images to JPEG.')

            pool = Pool()
            pool.map(self.convert_image, photo_files)

            print(f'\nConversion complete.')
        
        except KeyboardInterrupt:
            print(f'Conversion cancelled.')
        
        self.final_size = self.get_folder_stats(self.image_folder)
        print(f'''
Initial Folder Size: {round(self.init_size/1000000, 2)} MB
Final Folder Size: {round(self.final_size/1000000, 2)} MB
''')
        print(f'{self.percent_change()}% reduction in final directory size\n')

    def get_folder_stats(self, directory):
        size = 0
        for directory, _, files in walk(directory):
            for file in files:

                filepath = path.join(directory, file)
                size += path.getsize(filepath)
        return size

    def percent_change(self):
        p_c = ((self.init_size - self.final_size) / self.init_size) * 100
        return round(p_c, 2)

    def convert_image(self, photo_path):
        converted_path = f'{path.splitext(photo_path)[0]}.jpg'
        if not path.exists(converted_path) or self.replace:
            try:
                with rawpy.imread(photo_path) as raw:
                    rgb = raw.postprocess(
                        gamma=(1.25, 4.5),
                        bright=1.1,
                        no_auto_bright=False,
                        use_camera_wb=True
                    )

                imageio.imsave(converted_path, rgb)
                print(f'Exported image: {converted_path}')

            except Exception as e:
                print(f'Error loading file {photo_path}')

        if self.delete_old:
            # print(f'Deleted file: {photo_path}')
            remove(photo_path)

if __name__ == '__main__':
    try:
        d = args.directory[0]
    except TypeError:
        d = str(input('\nPhotos Folder: '))

    RawToJpeg(image_folder=d, delete_old=args.remove_old, replace=args.overwrite)
