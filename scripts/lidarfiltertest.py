import unittest
import numpy as np

from lidarfilter import LidarFilter

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.data1 = np.full(360, 0.6)
        self.data1[0:5] = 0.3
        self.data1[354:360] = 0.3
        self.lu1 = LidarFilter(36)

        self.data2 = [0.3]*360
        self.data2[270:360] = [0.4]* 90
        self.data2[0:90] = [0.3] * 90


    def test_data(self):
        self.assertEqual(len(self.data1), 360)

    def test_detect(self):
        self.lu1.data(self.data1, min=0, max=2)
        self.assertTrue(self.lu1.minpos == 0)

    def test_detect1(self):
        self.lu2 = LidarFilter(4)
        self.lu2.data(self.data2, min=0, max=2)
        self.assertAlmostEqual(self.lu2.min, 0.3, 2)
        self.assertEqual(self.lu2.minpos, 1)

    def test_detect3(self):
        lu3 = LidarFilter(36)
        data3 = [0.3] * 360
        data3[185] = 0.2
        lu3.data(data3, min=0, max=2)
        self.assertAlmostEqual(lu3.min, 0.29, 2)
        self.assertEqual(lu3.minpos, 19)

if __name__ == '__main__':
    unittest.main()
