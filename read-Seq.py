import cv2
import pims
import os
import numpy as np
from os.path import join, exists

path = r'Z:\Geeta-Share\DiffFileFormats\seq'
outputDir = join(r'Z:\Geeta-Share\DiffFileFormats', 'Output-Png')

for subpath, dirs, files in list(os.walk(path)):
    output_subpath = subpath.replace(path, outputDir)
    if not exists(output_subpath):
        os.mkdir(output_subpath)
        
    files = [f for f in files if f.endswith('seq')]
    if len(files) > 0:
        for fname in files:
            input_fname = join(subpath, fname)
            this_foldername = join(output_subpath, fname.replace('.seq', ''))
            if not exists(this_foldername):
                os.mkdir(this_foldername)
            vid = pims.open(input_fname)
            num_frames = vid._image_count
            for n in range(num_frames):
                img = vid.get_frame(n)
                img = ((img - img.min()) * 1.0 /  (img.max() - img.min()) * 255).astype(np.uint8)
                to_save_path = join(this_foldername, '{0}.png'.format(n))
                cv2.imwrite(to_save_path, img)
