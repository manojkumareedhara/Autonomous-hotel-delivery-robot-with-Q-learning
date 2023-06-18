#!/usr/bin/python3
import rospy
from geometry_msgs.msg import PointStamped
import tf
import random
import csv
import numpy as np

global x,y,z
x = 0.0
y = 0.0
z = 0.0

def create_point_cloud(*point):
    with open("my_coordinates.csv","a",encoding="UTF8",newline="") as f:
        writer =csv.writer(f)
        writer.writerow(point)
    
    

def callback(msg): 
    point = PointStamped()
    point.header.stamp = rospy.Time.now()
    point.header.frame_id = "/map"
    point.point.x = msg.point.x
    point.point.y = msg.point.y 
    point.point.z = msg.point.z
    print(point.point.x,point.point.y,point.point.z)
    #print(point)
    #create_point_cloud(point.point.x,point.point.y,point.point.z)
    
    


def listener():
    rospy.init_node('goal_publisher', anonymous=True)
    rospy.point_pub = rospy.Subscriber('/clicked_point', PointStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()