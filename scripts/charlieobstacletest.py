import unittest
import numpy as np

from charlieobstacle import CharlieObstacle

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.data0 = np.full(360, 0.30)
        self.data1 = np.random.uniform(30, 31, size=360)
        self.data2 = np.random.uniform(31, 32, size=360)
        self.data3 = np.random.uniform(32, 33, size=360)
        self.co = CharlieObstacle(0.3) # meters

    def test_data(self):
        self.assertEqual(len(self.data1), 360)

    def test_degrees(self):
        self.assertEqual(self.co.degrees(0, self.data0), 0.30)

    def test_obstacle(self):
        self.assertEqual(self.co.obstacle(0, self.data0), False)

if __name__ == '__main__':
    unittest.main()
