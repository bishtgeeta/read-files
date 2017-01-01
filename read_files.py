import imageio
import os
from os.path import join, exists


def readAvi(input_path, output_path, first_frame=None, last_frame=None):
    
    reader = imageio.get_reader(input_path)
    for i, img in enumerate(reader):
        imageio.imwrite(
    

def readAVI(inputPath, outputPath=None, firstFrame=None, lastFrame=None):

    reader = imageio.get_reader(inputPath)
    col, row = reader.get_meta_data()['size']

    if firstFrame is None:
        firstFrame = 0
    if lastFrame is None:
        lastFrame = reader.get_meta_data()['nframes'] - 1
    
    if outputPath is not None:    
        metadataFile = open(join(outputPath, 'metadata.txt'))
        ## TODO - write metadata
        
        metadataFile.close()
    
    numFrames = lastFrame - firstFrame
    gImgRawStack = numpy.zeros([row,col,numFrames],dtype='uint8')
    for i, img in enumerate(reader):
        if i < firstFrame or i > lastFrame:
            continue
        
        imageNum = i - firstFrame
        gImgRawStack[:,:,imageNum] = img[:,:,0]
        if output_path is not None:
            fname_to_write = join(output_path, '{0}.png'.format(i))
            imageio.imwrite(fname_to_write, img[:,:,0])
            
    reader.close()
    return gImgRawStack,row,col,numFrames

input_dir = r"F:\Python\EMImagingMPI-master"
input_file = r"F:\Python\EMImagingMPI-master\38-crop.avi"

output_file = join(input_dir, 'output.mp4')

readAVI('alana', 'falana', firstFrame=1000, lastFrame=1500)
    

    
readAvi(input_dir, output_dir)

#~ l = ['paht', 'outoutpathj']
#~ d =  {'fist_frame': 4, 'last_frame': 5}

#~ readavi(*l, **d}
