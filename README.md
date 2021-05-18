# RAW-to-JPEG

This program converts all RAW images in a directory and into to JPEGS. It's a fairly simple program, but I plan to add more features as time goes on such as auto-white balance and auto exposure adjustments. Great for converting a bunch of photos you don't really care about to save space.

## Instructions:
To get started, all you have to do is paste your starting directory in the spot that says `folder = ''`. When you hit run, it'll go through every file and folder in that file. If it ends with the RAW extension, it'll save a copy of that image as a jpeg. Simple stuff.

## Dependencies:
This program uses [rawpy](https://pypi.org/project/rawpy/) and [imageio](https://imageio.readthedocs.io/en/stable/sec_gettingstarted.html). To install, run the following command:
`pip3 install rawpy imageio`
