import unittest
import numpy as np

from lidarutils import LidarUtils

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.data1 = np.full(360, 0.5)
        self.lu = LidarObstacle(0.75, 30)

    def test_data(self):
        self.assertEqual(len(self.data1), 360)

    def test_detect(self):
        self.lu.data(self.data1)
        self.assertEqual(self.detect())
