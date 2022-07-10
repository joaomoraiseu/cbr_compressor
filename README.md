# cbr_compressor

A Python script that compress CBR (Comic book Rar) Files. Usage:

python compress_cbr.py PATH_OF_FILES COMPRESSION_LEVEL

where:

* PATH_OF_FILES: Path containing the CBR files. The script loop through folders and subfolders, converting all CBR files in it.
* COMPRESSION_LEVEL: The quality of the final compression. 100 it's the original size. At the end, of the proccess, the original it's replaced with the new file. The name of the file will be #####_compressed.cbr.

This script only works with CBR files. CBZ and other comic book formats are not supported.

For some reason, some files are not working with patool. The name of this files are in the file errors.txt, created by the script.

Dependencies:

Please instal the following libraries: 

* pip install rar 
* pip install patool
*  pip install pillow
