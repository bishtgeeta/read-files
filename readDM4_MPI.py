import cv2
import pims
import os
import numpy as np
from os.path import join, exists
import mpi4py
from mpi4py import MPI
import numpy

#######################################################################
# INITIALIZATION FOR THE MPI ENVIRONMENT
#######################################################################
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
#######################################################################

pathList = [
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\001',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\003',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\006',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\007',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\012',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\019',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\021',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\022',
#r'Z:\Geeta-Share\cubes assembly\20160614\one view\023'
#r'Z:\ShuFen-Share\20170217 assembly\003',
#r'Z:\ShuFen-Share\20170217 assembly\006',
#r'Z:\ShuFen-Share\20170228\006',
#r'Z:\ShuFen-Share\20170228\009',
r'Z:\ShuFen-Share\20170217\021',
r'Z:\ShuFen-Share\20170217\022'
]
outputDirList = [
#r'Z:\Geeta-Share\cubes assembly\20160614-001-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-003-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-006-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-007-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-012-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-019-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-021-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-022-output',
#r'Z:\Geeta-Share\cubes assembly\20160614-023-output'
#r'Z:\Geeta-Share\rod assembly\20170228-006-output',
#r'Z:\Geeta-Share\rod assembly\20170228-009-output',
r'Z:\Geeta-Share\bipyramid assembly\20170217-021-output',
r'Z:\Geeta-Share\bipyramid assembly\20170217-022-output'
]



for path,outputDir in zip(pathList,outputDirList):
    if (rank==0):
        print path
    inputFileList = []
    numFrames = 0

    if (rank==0):
        if not exists(outputDir):
            os.mkdir(outputDir)
    comm.Barrier()
            
    for subpath, dirs, files in list(os.walk(path)):
        files = [f for f in files if f.endswith('dm4')]
        for fname in files:
            inputFileList.append(join(subpath, fname))
            numFrames+=1
            
    inputFileList = sorted(inputFileList)
    frameList = range(1,numFrames+1)
    procFrameList = numpy.array_split(frameList,size)
    procInputFileList = numpy.array_split(inputFileList,size)
    
    for frame,inputFile in zip(procFrameList[rank],procInputFileList[rank]):
        outputFile = outputDir+'/'+str(frame).zfill(6)+'.png'
        img = pims.Bioformats(inputFile)
        img_array = img.get_frame(0)
        img_array = img_array.astype(int)
        p_low,p_high = np.percentile(img_array.flatten(), [.01,99.99])
        img_array[img_array <= p_low] = p_low
        img_array[img_array >= p_high] = p_high
        img_array = ((img_array - img_array.min()) * 1.0 /  (img_array.max() - img_array.min()) * 255).astype(np.uint8)
        cv2.imwrite(outputFile, img_array)
    comm.Barrier()
