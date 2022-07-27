import PIL
import PIL.Image
import patoolib
import tempfile
import os
import argparse

def compress_cbr(input_path,output_path,compression_level):
	cbrName = input_path.split('/').pop().split(".")[0]
	try:
		with tempfile.TemporaryDirectory() as tmpdirname:
			patoolib.extract_archive(input_path, outdir= tmpdirname)
			with tempfile.TemporaryDirectory() as compressedTmpDirName:
				compressedFilenames = []
				for filename in os.listdir(tmpdirname + "/" + cbrName):
					if ".jpg" in filename or ".png" in filename:
						img = PIL.Image.open(tmpdirname + "/" + cbrName + "/" + filename)
						myHeight, myWidth = img.size
						threshold = int(compression_level)
						newHeight = (myHeight * threshold) / 100
						newWidth = (myWidth * threshold) / 100
						img = img.resize((int(newHeight), int(newWidth)), PIL.Image.ANTIALIAS)
						compressedFilename = compressedTmpDirName + "/" + filename
						compressedFilenames.append(compressedFilename)
						img.save(compressedFilename)
				output_file = output_path + "/" + cbrName + "_compressed"
				patoolib.create_archive(output_file + ".zip", compressedFilenames)
				os.rename(output_file + ".zip",output_file + ".cbr")
				os.remove(input_path)
	except Exception as e:
		with open("erros.txt", 'a') as f:
			f.write(cbrName + "\n")

parser = argparse.ArgumentParser(description="",formatter_class=argparse.RawTextHelpFormatter,)
parser.add_argument("input_path", nargs="+", help="Path of the CBR")
parser.add_argument("compression_level", nargs="+", help="Level of compression (e.g 90% of the original etc...")

args = parser.parse_args()
input_path = args.input_path[0]

for root, dirs, files in os.walk(input_path):
	for file in files:
		if "_compressed" not in file and ".cbr" in file:
			compress_cbr(os.path.join(root, file),root,args.compression_level[0])
