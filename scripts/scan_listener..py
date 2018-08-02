#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from easy_filter.msg import Obstacle
import numpy as np

def callback(msg):
    if (msg.ranges[0] < 0.15):
        report_obstacle(msg.ranges[0])

def report_obstacle(dist):
    print ("Measured obstacle at" , dist)
    obstacle = Obstacle()
    obstacle.distance = dist
    pub.publish(obstacle)

if __name__ == '__main__':
    rospy.init_node('easy_listener')
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    pub = rospy.Publisher('obstacle',Obstacle, queue_size =10)
    rospy.spin()

