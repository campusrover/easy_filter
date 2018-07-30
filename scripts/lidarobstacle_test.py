import unittest
import numpy as np

from lidarobstacle import LidarObstacle

class MyFirstTests(unittest.TestCase):

    def setUp(self):
        self.data1 = np.random.uniform(30, 31, size=360)
        self.data2 = np.random.uniform(31, 32, size=360)
        self.data3 = np.random.uniform(32, 33, size=360)
        self.lo1 = LidarObstacle()

    def testData(self):
        self.assertEqual(len(self.data1), 360)
    
    def testMeasureOnce(self):
        self.lo1.measure(1, self.data1, 0)
        self.assertAlmostEqual(self.lo1.new_reading, 30.25, 0)

    def testTwice(self):
        self.lo1.measure(1, self.data1, 0)
        self.lo1.update()
        self.lo1.measure(2, self.data2, 0)
        self.lo1.update()
        self.assertAlmostEqual(self.lo1.reading, 30.75, 0)
    
    def testThrice(self):
        self.lo1.measure(1, self.data1, 0)
        self.lo1.update()
        self.lo1.measure(2, self.data2, 0)
        self.lo1.update()
        self.lo1.measure(3, self.data3, 0)
        self.lo1.update()
        self.assertAlmostEqual(self.lo1.reading, 31.5, 0)

if __name__ == '__main__':
    unittest.main()
