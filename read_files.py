import numpy as np
import imageio
import hyperspy
import os
from os.path import join, exists, isfile

def save_npy(path, array):
	np.save(path, array)


def readFromImageGenerator(imageGenerator, outputPath=None, 
								firstFrame=0, lastFrame=np.inf):
	
	## use set instead of list for faster add (instead of append) 
	gImgRawStack = set()
    for i, img in enumerate(imageGenerator):
        if i < firstFrame or i > lastFrame:
            continue
        imageNum = i - firstFrame
        gImgRawStack.add(img[:,:,0].astype(np.uint8))
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
	
def readdm3Sequence(inputPath, outputPath=None, firstFrame=0, lastFrame=np.inf)
	
	# TODO: check input and output paths	
	dm3Files = [f for f in os.listdir(inputPath) if f.endswith('dm3')]
	dm3Files.sort(key=lambda x: x.split('.')[0])
	## generator expression for images to avoid memory overload
	dm3Images = (hyperspy.load(join(inputPath,f)) for f in dm3Files)
	row, col = dm3Images[0].shape
	
	gImgRawStack, numFrames = readFromImageGenerator(dm3Images, 
						  outputPath=outputPath, firstFrame=firstFrame,
						  lastFrame=lastFrame)
						  
		
	return gImgRawStack, row, col, numFrames

def func(fileExtension='png', imageLoader=imageio.read):
	# TODO: check input and output paths
	def readImgSequence(inputPath, outputPath=None, firstFrame=0, lastFrame=np.inf)
		imgFiles = [f for f in os.listdir(inputPath) if f.endswith(fileExtension)]
		imgFiles.sort(key=lambda x: x.split('.')[0])
		## generator expression for images to avoid memory overload
		images = (imageLoader(join(inputPath,f)) for f in imgFiles)
		row, col = images[0].shape
		
		gImgRawStack, numFrames = readFromImageGenerator(images, 
							  outputPath=outputPath, firstFrame=firstFrame,
							  lastFrame=lastFrame)
			
		return gImgRawStack, row, col, numFrames
	
	return readImgSequence

readPngSequence = func(fileExtension='png', imageLoader=imageio.imread)
readDm3Sequence = func(fileExtension='dm3', imageLoader=hyperspy.load)
readDm4Sequence = func(fileExtension='dm4', imageLoader=hyperspy.load)

#~ gImgRawStack, row, col, numFrames = readPngSequence(
#~                      'input/path/to/images', 'output/path', 10, 50) 


	
	
