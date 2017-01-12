import cv2
import pims
import os
import numpy as np
from os.path import join, exists

path = r'F:\Python\EMImagingMPI-master'
outputDir = join(path, 'output-tif')

for subpath, dirs, files in list(os.walk(path)):
    output_subpath = subpath.replace(path, outputDir)
    if not exists(output_subpath):
        os.mkdir(output_subpath)
        
    files = [f for f in files if f.endswith('tif')]
    if len(files) > 0: 
        for fname in files:
            input_fname = join(subpath, fname)
            ## make a folder corresponding to every input seq file
            this_foldername = join(output_subpath, fname.replace('.seq', ''))
            if not exists(this_foldername):
                os.mkdir(this_foldername)
            vid = pims.open(input_fname)
            ## need to find how many frames are there in vid
            ## when you print dir(vid), you can see an attribute called `_image_count`
            num_frames = vid._read_metadata
            for n in range(num_frames):
                img = vid.get_frame(n)
                img = ((img - img.min()) * 1.0 /  (img.max() - img.min()) * 255).astype(np.uint8)
                to_save_path = join(this_foldername, '{0}.png'.format(n))
                cv2.imwrite(to_save_path, img)
