import unittest
import numpy as np

from lidarobstacle import LidarObstacle

class MyFirstTests(unittest.TestCase):

    def setUp(self):
        self.data1 = np.random.uniform(30, 31, size=360)
        self.data2 = np.random.uniform(31, 32, size=360)
        self.data3 = np.random.uniform(32, 33, size=360)

    def testData(self):
        self.assertEqual(len(self.data1), 360)

    def testFocus(self):
        lo1 = LidarObstacle(time=0, data=self.data1)
        self.assertAlmostEqual(lo1.get_instant_max(), 30.75, places=0)

    def testOnestep(self):
        lo1 = LidarObstacle(time=0, data=self.data1)
        onestep = LidarObstacle(time=1, data=self.data2, sofar=lo1)
        self.assertAlmostEqual(onestep.value_prime, 0.5, places=0)

if __name__ == '__main__':
    unittest.main()
