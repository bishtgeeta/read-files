import cv2
import pims
import os
from os.path import join, exists

path = r'C:\Users\dbsgbis\Desktop\001'
outputDir = join(path, 'output-png')


if not exists(outputDir):
	os.mkdir(outputDir)

fList = []

for subpath, dirs, files in os.walk(path):
    for f in files:
        if f.endswith('dm4'):
            fList.append(join(subpath, f))
        

fList.sort(key=lambda x: int(x.split('.')[0].split('_')[-1]))      
for fname in fList:
    img = pims.Bioformats(fname.encode('string_escape'))
    img_array = img.get_frame(0)
    output_fname = fname.replace('dm4', 'png') 
    cv2.imwrite(join(outputDir, output_fname), img_array)
