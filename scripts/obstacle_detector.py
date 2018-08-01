#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from easy_filter.msg import Obstacle
import numpy as np

class ObstacleDetector():

    def __init__(self, min_distance, beam_width):
        print("init")
        self.sub = rospy.Subscriber('scan', LaserScan, self.scan, queue_size=1)
        self.pub = rospy.Publisher('obstacle', Obstacle, queue_size =10)
        self.min_distance = min_distance
        self.beam_width = beam_width
        self.detect()

    def scan(self, scan):
        dist = scan.ranges[0]
        if (dist >= scan.range_min and dist < scan.range_max):
            if (dist < self.min_distance):
                self.report_obstacle(dist)


    def detect(self):
        while not rospy.is_shutdown():
            rospy.spin()

    def report_obstacle(self, dist):
        print ("Measured obstacle at" , dist)
        obstacle = Obstacle()
        obstacle.distance = dist
        self.pub.publish(obstacle)


def main():
    rospy.init_node('obstacle_detector')
    try:
        obdetect = ObstacleDetector(0.3, 10)
    except rospy.ROSInterruptException:
        print("Exception")

if __name__ == '__main__':
    main()
    print("clean exit")