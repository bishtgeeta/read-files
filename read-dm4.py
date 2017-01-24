import cv2
import pims
import os
import numpy as np
from os.path import join, exists

path = r'C:\Users\dbsgbis\Desktop\002'
outputDir = join(path, 'output-png')

for subpath, dirs, files in list(os.walk(path)):
    output_subpath = subpath.replace(path, outputDir)
    if not exists(output_subpath):
        os.mkdir(output_subpath)
        
    files = [f for f in files if f.endswith('dm4')]
    if len(files) > 0:
        for fname in files:
            input_fname = join(subpath, fname)
            output_fname = join(output_subpath, fname).replace('dm4', 'png')
            img = pims.Bioformats(input_fname)
            img_array = img.get_frame(0)
            img_array = img_array.astype(int)
            img_array = ((img_array - img_array.min()) * 1.0 /  (img_array.max() - img_array.min()) * 255).astype(np.uint8)
            cv2.imwrite(output_fname, img_array)
