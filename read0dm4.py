import cv2
import pims
import os
from os.path import join, exists

path = r'C:\Users\dbsgbis\Desktop\001'
outputDir = join(path, 'output-png')




for subpath, dirs, files in os.walk(path):
    output_subpath = subpath.replace(path, outputDir)
    os.mkdir(output_subpath)
    files = [f for f in files if f.endswith('dm4')]
    if len(files) > 0:
        
        for fname in files:
            input_fname = join(subpath, fname)
            output_fname = join(output_subpath, fname)
            img = pims.Bioformats(input_fname)
            img_array = img.get_frame(0)
            img_array = ((img_array - img_array.min())  /  (img_array.max() - img_array.min()) * 255).astype(np.uint8)
            output_fname = fname.replace('dm4', 'png')
            cv2.imwrite(output_fname, img_array)
