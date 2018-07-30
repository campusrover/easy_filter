#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

def callback(msg):
    print ("***********")
    print (type(msg.ranges[0]))
    a = np.array(msg.ranges)
    print(len(a))

rospy.init_node('easy_listener')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()

