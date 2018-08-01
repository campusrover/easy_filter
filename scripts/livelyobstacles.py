#!/usr/bin/env python
import rospy
import sys, select, termios, tty
from easy_filter.msg import Obstacle
from geometry_msgs.msg import Twist
import numpy as np

class LivelyObstacles():

    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('obstacle', Obstacle, self.obstacle_detected)
        self.obstacle = 0

    def scan(self, scan):
        dist = scan.ranges[0]
        print(dist)
        if (dist >= scan.range_min and dist < scan.range_max):
            print(dist)
            if (dist < 0.3):
                self.report_obstacle(scan.ranges[0])

    def bumper(self):
        while not rospy.is_shutdown():
            rospy.spin()

    def report_obstacle(self, dist):
        print ("Measured obstacle at" , dist)
        obstacle = Obstacle()
        obstacle.distance = dist
        self.pub.publish(obstacle)

    def circle_step(self):
        print("Circle step")
        twist = Twist()
        twist.linear.x = 0.07; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.2
        self.pub.publish(twist)

    def obstacle_detected(self, msg):
        print("obstacle detected")
        self.obstacle = 20

    def avoidance_step():
        print("avoidance step")
        twist = Twist()
        twist.linear.x = -0.02; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.3
        self.pub.publish(twist)

    def travel(self):
        print("travel")
        while(not rospy.is_shutdown()):
            if (self.obstacle > 0):
                self.avoidance_step()
                self.obstacle -= 1
            #else:
                #self.circle_step()
    
    def full_stop(self):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        self.pub.publish(twist)


def main():
    rospy.init_node('livelyobstacles')
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

