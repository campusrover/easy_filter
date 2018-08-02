#!/usr/bin/env python
import rospy
import sys, select, termios, tty
from easy_filter.msg import Obstacle
from geometry_msgs.msg import Twist
import numpy as np

class Esp():

    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=25)
        self.sub = rospy.Subscriber('obstacle', Obstacle, self.obstacle_reported)
        self.twist = Twist()
        self.obstacle = 0

    def obstacle_reported(self, msg):
        self.distance = msg.distance
        self.direction = msg.direction
        self.max_direction = msg.maxdirection
        if(self.direction == 0):
            self.obstacle = 5
            print("obstacle:", msg.distance, msg.direction)

    def decide(self):
        if (self.obstacle == 0):
            speed = 0.07
            turn = 0.0
        else:
            speed = -0.03
            turn = 0.2
            self.obstacle -= 1
        self.set_twist(speed, turn)

    def set_twist(self, speed, turn):
        self.twist.linear.x = speed; self.twist.linear.y = 0.0; self.twist.linear.z = 0.0
        self.twist.angular.x = 0.0; self.twist.angular.y = 0.0; self.twist.angular.z = turn
        print(self.twist)

    def travel(self):
        self.rate = rospy.Rate(10)
        while(not rospy.is_shutdown()):
            self.decide()
            self.pub.publish(self.twist)
            self.rate.sleep()
    
    def full_stop(self):
        print("FullStop")
        self.set_twist(0.0, 0.0)
        self.pub.publish(self.twist)


def main():
    rospy.init_node('livelyobstacles')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=25)
    esp = Esp()

    try:
        esp.travel()
    except rospy.ROSInterruptException:
        print("Exception")
    finally:
        esp.full_stop()

if __name__ == '__main__':
    main()
    print("clean exit")

