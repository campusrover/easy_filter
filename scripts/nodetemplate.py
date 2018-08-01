#!/usr/bin/env python
# Put all the imports here
import rospy
from sensor_msgs.msg import LaserScan
from easy_filter.msg import Obstacle

# One class to contain all the functionality and keep it separate
class ObstacleDetector():

    def __init__(self):
        # here is where you create your topic subscribers etc
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan, queue_size=1)
        self.pub = rospy.Publisher('obstacle', Obstacle, self.scan, queue_size =10)

        # And then you laucn the functionality
        self.bumper()

    def scan(self, scan):
        dist = scan.ranges[0]
        if (dist >= scan.range_min and dist < scan.range_max):
            print(dist)
            if (dist < 0.3):
                self.report_obstacle(scan.ranges[0])

    # Main loop is here
    def bumper(self):
        while not rospy.is_shutdown():
            rospy.spin()

    def report_obstacle(self, dist):
        print ("Measured obstacle at" , dist)
        obstacle = Obstacle()
        obstacle.distance = dist
        self.pub.publish(obstacle)


# Outside the class we have a method which creates the node, and catches exceptions
def main():
    rospy.init_node('obstacle_detector')
    try:
        obdetect = ObstacleDetector()
    except rospy.ROSInterruptException:
        print("Exception")

# And the python main for the file just calls main
if __name__ == '__main__':
    main()
    print("clean exit")