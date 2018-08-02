import numpy as np

class LidarUtils():
    def __init__(self, min_distance, beam_width):
        self.min_distance = min_distance
        self.beam_width = beam_width
        self.distance = -1
        self.direction = -1

    def data(self, data_array):
        assert(len(data_array)==360)
        left_part = np.array(data[360-beam_width/2:359])
        right_part = np.array(data[0:beam_width/2])
        focus_part = np.concatenate((left_part, right_part))
        self.direction = 0
        self.distance = np.average(focus_part)

    def detect(self):
        return(self.distance < self.min_distance)

