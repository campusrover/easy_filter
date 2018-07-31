import numpy as np

class CharlieObstacle():
    def __init__(self, distance):
        self.distance = distance
    
    def degrees(self, angle, data):
        return(data[angle])
    
    def obstacle(self, angle, data):
        return(data[angle < self.distance])
    
