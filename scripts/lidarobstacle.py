import numpy as np

class LidarObstacle():
    def __init__(self):
        self.reading = 30
        self.noise = 0
        self.time = 0
    
    def measure(self, time, data, noise):
        left_part = np.array(data[360-15:359])
        right_part = np.array(data[0:15])
        focus_part = np.concatenate((left_part, right_part))
        self.new_reading = np.percentile(focus_part, 25)
        self.new_noise = noise
        self.new_time = time

    def update(self):
        self.reading = (self.new_reading + self.reading)/2
        self.noise = self.new_noise
        self.time = self.new_time

    