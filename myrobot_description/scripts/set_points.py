#!/usr/bin/python3

import rospy
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import PoseStamped

import actionlib

#move_base_msgs
from move_base_msgs.msg import *
from geometry_msgs.msg import *

import tf
import random
import numpy as np
import pandas as pd

   

    
class co_ord():

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.room_coordinates = []
        self.d = None
        self.x_pos=0
        self.y_pos =0
        
        
    
    def callback(self,msg):
        #global d
        self.d = msg.pose.pose.position
        self.x_pos = msg.pose.pose.position.x
        self.y_pos= msg.pose.pose.position.y
        

    def talker(self,p,i):

        rospy.init_node('talker','read_pose', anonymous=True)
        sac = actionlib.SimpleActionClient('move_base/goal', MoveBaseAction )
        
        #create goal
        goal = MoveBaseGoal()
        goal.target_pose.pose = p
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
         
         
        #start listner
        sac.wait_for_server()
        #send goal
        sac.send_goal(goal)
        print("Sending goal:", i)
        #finish
        sac.wait_for_result()
        result = MoveBaseActionResult
        print(sac.get_result(), "Reached : ",i)  
        

    
        
        
    
        

if __name__ == '__main__':

    df = pd.read_csv('my_poses2.csv')
    df = df.iloc[:,1:]
    o_seq = []
    for i in range(0,20):
        a = []
        for j in range(3,7):
            a.append(df.iloc[i,j])
    o_seq.append(a)
        
    p_seq = []
    for i in range(0,20):
        a = []
        for j in range(0,3):

            a.append(df.iloc[i,j])
            p_seq.append(a)
        
        
    oo_q = []
    for q in o_seq:
        oo_q.append(Quaternion(*q))

    pp_seq = []
    for point in p_seq:
        i = 0
        pp_seq.append(Pose(Point(*point),oo_q[i]))
        i = i + 1
    #print(pp_seq)
    i = 0
    arr = []
    #for r in range(20):
     #   arr.append(co_ord())
    
    while(i<21):
        
        arr.append(co_ord())
        p = pp_seq[i]        
        arr[i].talker(p,i)        
        i = i + 1
        #rospy.signal_shutdown("Moving to next goal")
    