#!/usr/bin/python3
import pandas as pd
import rospy
from move_base_msgs.msg import *
import actionlib
def talker(x,y,z):
    sac = actionlib.SimpleActionClient("move_base",MoveBaseAction)
    rospy.init_node("talker",anonymous=True)

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id="map"
    goal.target_pose.header.stamp=rospy.Time.now()
    goal.target_pose.pose.position.x =pos_x
    goal.target_pose.pose.position.y=pos_y
    goal.target_pose.pose.position.z=pos_z
    sac.send_goal(goal)
    rospy.loginfo("goal sent/.....")
    wait =sac.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
    else:
        return sac.get_result()

def get_coordinates():
    df = pd.read_csv('my_coordinates.csv')
    print(df)
    df = df.iloc[1:,1:]
    print(df)
    x = df['0'].loc[1]
    y = df['1'].loc[1]
    print(x,y)
    
    
    


if __name__== '__main__':
    get_coordinates()