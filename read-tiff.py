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
            this_foldername = join(output_subpath, fname.replace('.seq', ''))
            if not exists(this_foldername):
                os.mkdir(this_foldername)
            vid = pims.open(input_fname)
            img_stack = vid.get_frame(0)
            for img_num in range(img_stack.shape[0]):
                img = img_stack[img_num]
                img = ((img - img.min()) * 1.0 /  (img.max() - img.min()) * 255).astype(np.uint8)
                to_save_path = join(this_foldername, '{0}.png'.format(img_num))
                cv2.imwrite(to_save_path, img)
