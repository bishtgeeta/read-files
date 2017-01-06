import cv2
import pims
import os
import numpy as np
from os.path import join, exists

path = r'Z:\Geeta-Share\DiffFileFormats\seq'
outputDir = join(path, 'output-png')

for subpath, dirs, files in list(os.walk(path)):
    output_subpath = subpath.replace(path, outputDir)
    if not exists(output_subpath):
        os.mkdir(output_subpath)
        
    files = [f for f in files if f.endswith('seq')]
    if len(files) > 0:
        for fname in files:
            input_fname = join(subpath, fname)
            output_fname = join(output_subpath, fname)
            vid = pims.open(input_fname)
            for img in vid:
                _img = ((img - img.min()) * 1.0 /  (img.max() - img.min()) * 255).astype(np.uint8)
                cv2.imwrite(join(output_fname, img).png, _img)
