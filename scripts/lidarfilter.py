import numpy as np

class LidarFilter():
    def __init__(self, slices):
        assert slices > 0
        assert slices <= 36

        self.slices = slices
        self.distance = -1
        self.direction = -1
        self.deg_per_slice = 360 / slices

    def data(self, data_array):
        assert(len(data_array)==360)
        darray = np.array(data_array)
        darray = np.roll(darray, self.deg_per_slice/2)
        self.mean_per_slice = darray.reshape((self.slices, -1)).mean(axis=1)
        self.min = self.mean_per_slice.min()
        self.minpos = self.mean_per_slice.argmin()


    def detect(self):
        return(self.distance < self.min_distance)

