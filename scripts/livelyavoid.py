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
def circle_step():
    print("Circle step")
    twist = Twist()
    twist.linear.x = 0.07; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.2
    pub.publish(twist)

def obstacle_detected(msg):
    global obstacle
    print("obstacle detected")
    obstacle = 20
    print("obstacle detected!")

def avoidance_step():
    print("avoidance step")
    twist = Twist()
    twist.linear.x = -0.02; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.3
    pub.publish(twist)


def travel():
    global obstacle
    print("travel")
    while(True):
        key = getKey()
        sys.stdout.write("."); sys.stdout.flush()
        if (key == '\x03'):
            break
        if (obstacle > 0):
            avoidance_step()
            obstacle -= 1
        else:
            circle_step()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    obstacle = 0
    rospy.init_node('lively')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('obstacle', Obstacle, obstacle_detected)
    
    try:
        travel()
    except:
        print("Unexpected Exception", sys.exc_info())
    finally:
        print("Clean exit")
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
