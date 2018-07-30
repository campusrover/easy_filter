import numpy as np

class LidarObstacle():
    def __init__(self, time, data, sofar=None):
        self.data = self.focus(data)
        self.time = time
        self.instant_max = self.get_instant_max()
        if (sofar is not None):
            self.update_reading(sofar)

    def get_instant_max(self):
        return(np.percentile(self.data, 75))

    def focus(self, data):
        left_part = np.array(data[360-15:359])
        right_part = np.array(data[0:15])
        return(np.concatenate((left_part, right_part)))

    def update_reading(self, sofar):
        self.value = (sofar.instant_max - self.instant_max)/2
        self.elapsed = (sofar.time - self.time)
        self.value_prime = self.value / self.elapsed


    