#!/usr/bin/env python

import numpy as np

class LidarFilter():
    def __init__(self, slices):
        assert slices > 0
        assert slices <= 36

        self.slices = slices
        self.deg_per_slice = 360 / slices

    def data(self, data_array, min, max):
        assert(len(data_array)==360)
        darray = np.array(data_array)
        darray[darray <= min] = np.nan
        darray[darray > max] = np.nan
        darray = np.roll(darray, self.deg_per_slice/2)
        self.mean_per_slice = np.nanmean(darray.reshape((self.slices, -1)),axis=1)
        self.min = np.nanmin(self.mean_per_slice)
        self.minpos = np.nanargmin(self.mean_per_slice)
        print(self.min, self.minpos, self.mean_per_slice)


    def detect(self):
        return(self.distance < self.min_distance)

