#!/usr/bin/env python
import rospy
import sys, select, termios, tty
from easy_filter.msg import Obstacle
from geometry_msgs.msg import Twist
import numpy as np

# all this is to allow keystrokes and ^c to interrupt. Copied from teleop sample code.
def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

# Simple starting point, drives in a circle
def circle():
    twist = Twist()
    twist.linear.x = 0.07; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.2
    while(not facing_obstacle):
        key = getKey()
        sys.stdout.write("."); sys.stdout.flush()
        pub.publish(twist)
        if (key == '\x03'):
            break

def rotate_inplace():
    

def obstacle_detected(msg):
    facing_obstacle = True
    rotate_inplace()
    facing_obstacle = False

if __name__ == '__main__':
    facing_obstacle = False
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('lively')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('obstacle, Obstacle'. obstacle_detected)
    
    try:
        circle()
    except:
        print("Unexpected Exception", sys.exc_info())
    finally:
        print("Clean exit")
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
