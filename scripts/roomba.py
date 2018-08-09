#!/usr/bin/env python
import rospy
import sys, select, termios, tty
from easy_filter.msg import Obstacle
from geometry_msgs.msg import Twist
import numpy as np
import random

class Roomba():

    def __init__(self):
        print("Init")
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=25)
        self.sub = rospy.Subscriber('obstacle', Obstacle, self.obstacle_reported)
        self.state = 1
        self.last_state = 1
        self.direction = 3
        self.counter = 0
        

    def obstacle_reported(self, msg):
        # print("obstacle reported dir=%d dist=%f" % (msg.direction, msg.distance))
        self.direction = msg.direction
        self.distance = msg.distance

    def avoidance_step(self):
        twist = Twist()
        rotate_angle = 0.5
        if (self.direction == 1):
            print("%d turn neg" % (self.counter))
            rotate_angle = -0.5
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = rotate_angle
        self.pub.publish(twist)

    def straight_step(self):
        twist = Twist()
        twist.linear.x = 0.05; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        self.pub.publish(twist)

    def check_state(self):
        self.counter += 1
        if (self.direction == 1 or self.direction == 0 or self.direction == 5):
            self.state = 2
        else:
            self.state = 1
        if (self.state != self.last_state):
            print("%d State change from %d to %d" % (self.counter, self.last_state, self.state))
        self.last_state = self.state

    def travel(self):
        self.rate = rospy.Rate(10)
        while(not rospy.is_shutdown()):
            self.check_state()
            if (self.state == 1):
                self.straight_step()
            elif self.state == 2:
                self.avoidance_step()
            else:
                print("Invalid State")
            self.rate.sleep()
    
    def full_stop(self):
        print("FullStop")
        twist = Twist()
        self.rate = rospy.Rate(10)
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        for i in range(20):
            self.pub.publish(twist)
            self.rate.sleep()

def main():
    rospy.init_node('livelyobstacles')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=25)
    lively = Roomba()

    try:
        lively.travel()
    except rospy.ROSInterruptException:
        print("Exception")
    finally:
        lively.full_stop()

if __name__ == '__main__':
    main()
    print("clean exit")

