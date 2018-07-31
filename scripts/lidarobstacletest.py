import unittest
import numpy as np

from lidarobstacle import LidarObstacle

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.data1 = np.random.uniform(30, 31, size=360)
        self.data2 = np.random.uniform(31, 32, size=360)
        self.data3 = np.random.uniform(32, 33, size=360)
        self.lo1 = LidarObstacle()

    def test_data(self):
        self.assertEqual(len(self.data1), 360)

    def test_measureOnce(self):
        self.lo1.measure(1, self.data1, 0)
        self.assertAlmostEqual(self.lo1.new_reading, 30.25, 0)

    def test_twice(self):
        self.lo1.measure(1, self.data1, 0)
        self.lo1.update()
        self.lo1.measure(2, self.data2, 0)
        self.lo1.update()
        self.assertAlmostEqual(self.lo1.reading, 30.75, 0)
    
    def test_thrice(self):
        self.lo1.measure(1, self.data1, 0)
        self.lo1.update()
        self.lo1.measure(2, self.data2, 0)
        self.lo1.update()
        self.lo1.measure(3, self.data3, 0)
        self.lo1.update()
        self.assertAlmostEqual(self.lo1.reading, 31.5, 0)

class TestKalman(unittest.TestCase):

    def setUp(self):
        self.measurements = [5., 6. , 7., 9., 10.]
        self.motion = [1., 1., 2., 1., 1.]
        self.measurement_sig = 4.
        self.motion_sig = 2.
        self.mu = 0.
        self.sig = 10000.
        self.lo2 = LidarObstacle()
    
    def loop_test(self):
        val = [self.mu, self.sig]
        for i in range(len(self.measurements)):
            val = self.lo2.kalman_update(val[0], val[1], self.measurements[i], self.measurement_sig)
            val = self.lo2.kalman_predict(val[0], val[1], self.motion[i], self.motion_sig)
        print(val)
        
if __name__ == '__main__':
    unittest.main()
