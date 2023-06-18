#!/usr/bin/python3
import rospy,csv
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import _MoveBaseActionGoal
import numpy as np
import pandas as pd

class get_coordinates():
    def __init__(self):
        self.i=0
        #self.positions=[]
        #self.orientations=[]
    def create_point_cloud(self,*pose):
        with open("my_coordinates.csv","a") as f:
            rowwriter = csv.writer(f)
            rowwriter.writerow(pose)

    def callback(self,msg):
        #self.positions.append([msg.pose.position.x,msg.pose.position.y,msg.pose.position.z,msg.pose.orientation.x,msg.pose.orientation.y,msg.pose.orientation.z,msg.pose.orientation.w])
        #print("poses = ",self.positions)
        self.create_point_cloud(list([msg.pose.position.x,msg.pose.position.y,msg.pose.position.z,msg.pose.orientation.x,msg.pose.orientation.y,msg.pose.orientation.z,msg.pose.orientation.w]))
        print(msg.pose.position)



    def get_poses(self):
        print("hi2")
        #rospy.wait_for_message("/move_base_simple/goal",PoseStamped)
        print("hi3")
        rospy.init_node("goal_listener",anonymous = True)
        rospy.Subscriber("/move_base_simple/goal",PoseStamped,self.callback)
        rospy.spin()
    def full_array(self):
        return self.positions,

if __name__=="__main__":
    try:
        co_oordinates=get_coordinates()
        print("class created")
        co_oordinates.get_poses()
        
    
    except rospy.ROSInterruptException:
        rospy.loginfo("cancelled......................................")
