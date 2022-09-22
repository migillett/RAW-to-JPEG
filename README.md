# RAW-to-JPEG

This program converts all RAW images in a directory and into to JPEGS. It's a fairly simple program. Great for converting a bunch of photos you don't really care about to save space. My testing shows that it can reduce file sizes by up to 80%.

## Instructions:
1. Make sure you have Python3 installed. You can download the installer from the [Python Website](https://www.python.org/).
2. Clone the repository using `git clone https://github.com/migillett/RAW-to-JPEG`
3. While inside the newly downloaded git repo, install the dependencies using `pip3 install -r ./requirements.txt`
4. Run the program by doing `python3 ./raw_to_jpeg.py`.
5. Type out or paste your photos directory into the space given and press enter.

## Flags:
If you want to make this program dance a little more, you can use specific flags.

`-d` or `--directory` - Allows you to specific the directory you want to target

`-r` or `--remove` - Removes the RAW image files after conversion. Program default is to keep source files. USE WITH CAUTION!!

`-o` or `--overwrite` - Overwrites JPEG files when mass-converting. Program default is to skip over already converted files.

For example:
`python3 -r -o -d "/Volumes/archive/image folder"`

## Warnings:
Listen, you use this program at your own risk. If you enable the program to delete the master files, please have backups or be sure that you don't care about the files. I'm not responsible for any lost images, that's on you.

## Dependencies:
This program uses [rawpy](https://pypi.org/project/rawpy/) and [imageio](https://imageio.readthedocs.io/en/stable/sec_gettingstarted.html).

You can also find the program requirements in the `requirements.txt` file.
