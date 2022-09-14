import rawpy
import imageio
from os import path, walk, remove
from sys import exit
import multiprocessing

# https://www.pythontutorial.net/python-concurrency/python-multiprocessing/


class RawToJpeg():
    def __init__(self, image_folder, delete_old=False, replace=False) -> None:
        self.delete_old = delete_old
        self.replace = replace

        if self.delete_old:
            print('\nWARNING: the program is currently configured to delete old images. Are you sure?\n')
            confirm = input('Are you sure? (y/n):')
            if confirm != 'y':
                exit('\Conversion cancelled.\n')
    
        self.image_folder = image_folder

        self.extensions = ('.CR2', '.ARW', '.NEF', '.nef', '.cr2', '.arw', '.DNG', '.dng')

        processes = []

        images_processed = 0

        for directory, _, files in walk(self.image_folder):
            for file in files:
                if file.endswith(self.extensions):
                    filepath = path.join(directory, file)
                    processes.append(multiprocessing.Process(target=self.convert_image, args=[filepath]))
        
        print(f'Added {len(processes)} images for conversion.')

        print('Starting conversion...')
        
        for process in processes:
            process.start()

        for process in processes:
            process.join()
            images_processed += 1

        print(f'Conversion complete. {images_processed} images processed')

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
    RawToJpeg(image_folder=str(input('\nPhotos Folder: ')), delete_old=True)
