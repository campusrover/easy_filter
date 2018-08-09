#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from easy_filter.msg import Obstacle
import numpy as np
import lidarfilter as lu

class ObstacleDetector():

    def __init__(self, slice_count):
        self.sub = rospy.Subscriber('scan', LaserScan, self.scan, queue_size=1)
        self.pub = rospy.Publisher('obstacle', Obstacle, queue_size=1)
        self.slice_count = slice_count
        self.lf = lu.LidarFilter(slice_count) # 0, counterclockwise for the number slices.
        self.count = 0
    
    def scan(self, scan):
        self.lf.data(scan.ranges, scan.range_min, scan.range_max)
        if (self.lf.min <= 0.5):
            self.report_obstacle()

    def detect(self):
        while not rospy.is_shutdown():
            rospy.spin()

    def report_obstacle(self):
        print ("(%d) Obst detcted: dist=%f dir=%d" % (self.count, self.lf.min, self.lf.minpos))
        self.count += 1
        #print(self.lf.printraw())
        obstacle = Obstacle()
        obstacle.distance = self.lf.min
        obstacle.direction = self.lf.minpos # 0, 1, 2, 3...
        obstacle.maxdirection = self.slice_count
        self.pub.publish(obstacle)


def main():
    rospy.init_node('obstacle_detector')
    obdetect = ObstacleDetector(6)

    try:
        obdetect.detect()
    except rospy.ROSInterruptException:
        print("Exception")

if __name__ == '__main__':
    main()
    print("clean exit")