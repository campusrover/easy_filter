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
        [new_mean, new_noise] = self.kalman_update(self.reading, self.noise, self.new_reading, self.new_noise)
        self.reading = new_mean
        self.noise = new_noise
        self.time = self.new_time

    def kalman_update(self, mean1, var1, mean2, var2):
        new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
        new_var = 1 / (1 / var1 + 1 / var2)
        return [new_mean, new_var]

    