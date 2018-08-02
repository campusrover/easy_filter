#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from easy_filter.msg import Obstacle
import numpy as np
import lidarutils as lu

class ObstacleDetector():

    def __init__(self, slice_count):
        print("init")
        self.sub = rospy.Subscriber('scan', LaserScan, self.scan, queue_size=1)
        self.pub = rospy.Publisher('obstacle', Obstacle, queue_size =10)
        self.lu = lu.LidarUtils(4) # front=0, right=1, back=2, left=3

    def scan(self, scan):
        lu.data(scan.ranges)
        if (self.lu.min <= 0.3)):
            self.report_obstacle()

    def detect(self):
        while not rospy.is_shutdown():
            rospy.spin()

    def report_obstacle(self, dist):
        print ("Measured obstacle at" , dist)
        obstacle = Obstacle()
        obstacle.distance = self.lu.min()
        obstacle.direction = self.lu.minpos() # 0, 1, 2, 3
        self.pub.publish(obstacle)


def main():
    rospy.init_node('obstacle_detector')
    obdetect = ObstacleDetector(10)

    try:
        obdetect.detect()
    except rospy.ROSInterruptException:
        print("Exception")

if __name__ == '__main__':
    main()
    print("clean exit")