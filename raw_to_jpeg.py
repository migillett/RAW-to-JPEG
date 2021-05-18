import rawpy
import imageio
import os.path


def raw_to_jpeg(folder):
    extensions = ['.CR2', '.ARW']

    for directory, subdirectory, files in os.walk(folder):
        for file in files:
            photo_path = os.path.join(directory, file)
            for extension in extensions:
                if photo_path.endswith(extension):
                    converted_path = f'{os.path.splitext(photo_path)[0]}.jpg'
                    if not os.path.exists(converted_path):
                        with rawpy.imread(photo_path) as raw:
                            rgb = raw.postprocess()
                        imageio.imsave(converted_path, rgb)
                        print('Converted image:', converted_path)
    print('Done.')


if __name__ == '__main__':
    # put the starting directory here:
    folder = 'F:\PHOTOS'
    
    raw_to_jpeg(folder)
