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

class get_pose():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.ox = 0
        self.oy = 0
        self.oz = 0
        self.ow = 0
        
 
        
    
    

    
class co_ord():

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.room_coordinates = []
        self.d = None
        
    
    def callback(self,msg):
        #global d
        self.d = msg.pose.pose.position
        

    def talker(self,x,y,z):

        

        sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )
        rospy.init_node('talker','read_pose', anonymous=True)
        
        #create goal
        
        goal = MoveBaseGoal()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = 0.9 #997714974432653
        goal.target_pose.pose.orientation.z = z #.0237645667670314
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
         
         
        #start listner
        sac.wait_for_server()
        #send goal
        sac.send_goal(goal)
        print("Sending goal:")
        #finish
        sac.wait_for_result()
        result = MoveBaseActionResult
        #print(result)
        print("state",sac.get_state())
        print(sac.get_result(),"reached : ")

        
        #rospy.init_node("read_pose",anonymous =True)
        print("before")
        sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.callback)
        print('after')
        rate = rospy.Rate(10)
        print(self.d)
        rate.sleep() #Sleep at 10H

    

    
        
        
    
        

if __name__ == '__main__':

    df = pd.read_csv('my_coordinates.csv')
    df = df.iloc[1:,1:]
    print(df)
    print(df.iloc[1,0])
    co_ord = co_ord()
    for i in range(1,21):
        x = round(df['0'].loc[i],5)
        y = round(df['1'].loc[i],5)
        z = round(df['2'].loc[i],5)
        
        print(x,y)
        
        co_ord.talker(x,y,z)
        
        


       
   