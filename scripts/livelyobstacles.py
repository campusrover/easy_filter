#!/usr/bin/env python
import rospy
import sys, select, termios, tty
from easy_filter.msg import Obstacle
from geometry_msgs.msg import Twist
import numpy as np

class LivelyObstacles():

    def __init__(self):
        print("Init")
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=25)
        self.sub = rospy.Subscriber('obstacle', Obstacle, self.obstacle_reported)
        self.obstacle = 0
        
    def circle_step(self):
        twist = Twist()
        twist.linear.x = 0.07; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.2
        self.pub.publish(twist)

    def obstacle_reported(self, msg):
        print("obstacle detected")
        self.obstacle = 20

    def avoidance_step(self):
        twist = Twist()
        twist.linear.x = -0.04; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.1
        print(twist)
        self.pub.publish(twist)

    def travel(self):
        print("travel")
        self.rate = rospy.Rate(10)
        while(not rospy.is_shutdown()):
            if (self.obstacle > 0):
                self.avoidance_step()
                self.obstacle -= 1
            else:
                self.circle_step()
            self.rate.sleep()
    
    def full_stop(self):
        print("FullStop")
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        self.pub.publish(twist)


def main():
    rospy.init_node('livelyobstacles')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=25)
    lively = LivelyObstacles()

    try:
        lively.travel()
    except rospy.ROSInterruptException:
        print("Exception")
    finally:
        lively.full_stop()

if __name__ == '__main__':
    main()
    print("clean exit")

