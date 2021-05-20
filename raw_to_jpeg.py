import rawpy
import imageio
import os.path


def raw_to_jpeg(folder, delete_old=False):
    extensions = ['.CR2', '.ARW', '.NEF']
    images_processed = 0

    for directory, subdirectory, files in os.walk(folder):
        for file in files:

            photo_path = os.path.join(directory, file)

            for extension in extensions:
                if photo_path.endswith(extension):

                    converted_path = f'{os.path.splitext(photo_path)[0]}.jpg'
                    if not os.path.exists(converted_path):
                        with rawpy.imread(photo_path) as raw:
                            rgb = raw.postprocess(
                                gamma=(1.25, 4.5),
                                bright=1.1,
                                no_auto_bright=False,
                                use_camera_wb=True
                            )

                        imageio.imsave(converted_path, rgb)
                        print('Converted image:', converted_path)
                        images_processed += 1

                        if delete_old:
                            os.remove(photo_path)
                            print('Deleted file:', photo_path)

                    else:
                        print('Image already exported:', converted_path)

    print('Export Complete. Images processed:', images_processed)


if __name__ == '__main__':
    # put the starting directory here:
    photos_folder = 'F:\PHOTOS'
    raw_to_jpeg(photos_folder)
