# RAW-to-JPEG

This program converts all RAW images in a directory and into to JPEGS. It's a fairly simple program. Great for converting a bunch of photos you don't really care about to save space.

## Instructions:
To get started, all you have to do is paste your starting directory in the spot that says `folder = ''`. When you hit run, it'll go through every file and folder in that file. If it ends with the RAW extension, it'll save a copy of that image as a jpeg. Simple stuff.

The program also has a auto whitebalance and auto exposure settings. They're enabled by default, but you can turn this feature off by setting `auto_wb=False` and `auto_exp=False` when you call the `raw_to_jpeg` function.

You can also enable the `delete_old` parameter, which deletes the RAW images after it converts them to JPEG. USE AT YOUR OWN RISK!

## Dependencies:
This program uses [rawpy](https://pypi.org/project/rawpy/) and [imageio](https://imageio.readthedocs.io/en/stable/sec_gettingstarted.html). To install, run the following command:
`pip3 install rawpy imageio`

You can also find the program requirements in the `requirements.txt` file.
