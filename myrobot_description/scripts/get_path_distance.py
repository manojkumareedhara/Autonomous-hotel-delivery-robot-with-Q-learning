#!/usr/bin/python3
import rospy
from nav_msgs.msg import Path
import tf
import random

import numpy as np


    

def callback(path_msg):
    global path_length
    path_length = 0
    for i in range(len(path_msg.poses) - 1):
        position_a_x = path_msg.poses[i].pose.position.x
        position_b_x = path_msg.poses[i+1].pose.position.x
        position_a_y = path_msg.poses[i].pose.position.y
        position_b_y = path_msg.poses[i+1].pose.position.y

        path_length += np.sqrt(np.power((position_b_x - position_a_x), 2) + np.power((position_b_y- position_a_y), 2))
    rospy.loginfo(path_length)


def listener():
    rospy.init_node('goal_publisher', anonymous=True)
    rospy.path_sub = rospy.Subscriber("/move_base/DWAPlannerROS/global_plan", Path, callback)
    #rospy.point_pub = rospy.Subscriber('/clicked_point', PointStamped, callback_for_points)
    rospy.spin()

if __name__ == '__main__':
    listener()