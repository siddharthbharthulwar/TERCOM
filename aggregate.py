import numpy as np 
import gdal
import rasterio as rio 
import matplotlib.pyplot as plt
import numpy.ma as ma
import math
import cv2 as cv
from functions import harrisresponse


def parseString(ns, ew):


    masterPath = r"D:\Documents\School\2020-21\TerCoM\raw\{}_{}_1arc_v3.tif".format(ns, ew)
    return masterPath

def load(path):

    with rio.open(path) as src:

        lidar_dem_im = src.read(1, masked = True)
        arr = ma.masked_values(lidar_dem_im, np.amax(lidar_dem_im))
        return arr


n39w105 = r"D:\Documents\School\2020-21\TerCoM\raw\n39_w105_1arc_v3.tif"
n39w106 = r"D:\Documents\School\2020-21\TerCoM\raw\n39_w106_1arc_v3.tif"
n51e004 = r"D:\Documents\School\2020-21\TerCoM\raw\n51_e004_1arc_v3.tif"
n51e005 = r"D:\Documents\School\2020-21\TerCoM\raw\n51_e005_1arc_v3.tif"
n52e004 = r"D:\Documents\School\2020-21\TerCoM\raw\n52_e004_1arc_v3.tif"
n52e005 = r"D:\Documents\School\2020-21\TerCoM\raw\n52_e005_1arc_v3.tif"

dem = load(parseString("n39", "w106"))

plt.imshow(dem, cmap = 'terrain')
plt.show()
'''
plt.imshow(harrisresponse(dem) / np.amax(harrisresponse(dem)))
plt.show()

plt.imshow(harrisresponse(harrisresponse(dem)) / np.amax(harrisresponse(harrisresponse(dem))))
plt.show()
'''
plt.contour(dem, cmap = 'viridis', levels = list(range(0, 5000, 100)))
plt.show()