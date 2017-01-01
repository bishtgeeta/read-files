import numpy as np
import imageio
import os
from os.path import join, exists, isfile

def save_npy(path, array):
	np.save(path, array)


def readFromImageGenerator(imageGenerator, outputPath=None, 
								firstFrame=0, lastFrame=np.inf):
	
	gImgRawStack = []
    for i, img in enumerate(imageGenerator):
        if i < firstFrame or i > lastFrame:
            continue
        imageNum = i - firstFrame
        gImgRawStack.append(img[:,:,0].astype(np.uint8))
    gImgRawStack = np.array(gImgRawStack)
    numFrames = gImgRawStack.shape[2]
    if outputPath is not None:
		save_npy(outputPath, gImgRawStack)
		
	return gImgRawStack, numFrames

def readAVI(inputPath, outputPath=None, firstFrame=0, lastFrame=np.inf):
	
	# TODO: check input and output paths
    aviReader = imageio.get_reader(inputPath)
    col, row = aviReader.get_meta_data()['size']

    gImgRawStack, numFrames = readFromImageGenerator(reader, 
						  outputPath=outputPath, firstFrame=firstFrame,
						  lastFrame=lastFrame)
    
		
    return gImgRawStack, row, col, numFrames

def readPngSequence(inputPath, outputPath=None, firstFrame=0, lastFrame=np.inf)
	
	# TODO: check input and output paths	
	pngFiles = [f for f in os.listdir(inputPath) if f.endswith('png')]
	pngFiles.sort(key=lambda x: x.split('.')[0])
	## generator expression for images to avoid memory overload
	pngImages = (imageio.imread(join(inputPath,f)) for f in pngFiles)
	row, col = pngImages[0].shape
	
	gImgRawStack, numFrames = readFromImageGenerator(pngImages, 
						  outputPath=outputPath, firstFrame=firstFrame,
						  lastFrame=lastFrame)
		
	return gImgRawStack, row, col, numFrames







