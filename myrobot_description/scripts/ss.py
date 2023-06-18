#!/usr/bin/python3

import rospy
import math
import pandas as pd

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler


class MoveBaseSeq():

    def __init__(self, df):

        self.df = df
        self.goal_cnt = 0

        rospy.init_node('move_base_sequence', anonymous = True)

      
        #Create action client
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

        #waiting for server
        rospy.loginfo("Waiting for move_base action server...")
        wait = self.client.wait_for_server()
        t = self.client.wait_for_result()

        self.movebase_client()

    def active_cb(self):
            print("Goal pose "+str(self.goal_cnt+1)+" is now being processed by the Action Server...")

    def feedback_cb(self, feedback):
            #rospy.loginfo("Feedback for goal "+str(self.goal_cnt)+": "+str(feedback))
            print("Feedback for goal pose "+str(self.goal_cnt+1)+" received")

    def done_cb(self,status,result):
            status = self.client.get_state()
            self.goal_cnt += 1
            df1 = self.df.iloc[self.goal_cnt].to_numpy()
            if status == 3:
                rospy.loginfo("Goal pose "+str(self.goal_cnt)+" reached") 
                if self.goal_cnt< 6:
                    next_goal = MoveBaseGoal()
                    print(next_goal)
                    next_goal.target_pose.header.frame_id = "map"
                    next_goal.target_pose.header.stamp = rospy.Time.now()
                    next_goal.target_pose.pose.position.x = df1[0]
                    next_goal.target_pose.pose.position.y = df1[1]
                    next_goal.target_pose.pose.position.z = df1[2]
                    next_goal.target_pose.pose.orientation.x=df1[3]
                    next_goal.target_pose.pose.orientation.y= df1[4]
                    next_goal.target_pose.pose.orientation.z=df1[5] 
                    next_goal.target_pose.pose.orientation.w = df1[6]#997714974432653
                    rospy.loginfo("Sending goal pose "+str(self.goal_cnt+1)+" to Action Server")
                    #rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
                    self.client.send_goal(next_goal, self.done_cb, self.active_cb, self.feedback_cb) 
                else:
                    rospy.loginfo("Final goal pose reached!")
                    rospy.signal_shutdown("Final goal pose reached!")
                    return

        

    def movebase_client(self):
        df1 = self.df.iloc[self.goal_cnt].to_numpy()
    #for pose in pose_seq:   
        goal = MoveBaseGoal()
        print(goal)
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now() 
        goal.target_pose.pose.position.x = df1[0]
        goal.target_pose.pose.position.y = df1[1]
        goal.target_pose.pose.position.z = df1[2]
        goal.target_pose.pose.orientation.x=df1[3]
        goal.target_pose.pose.orientation.y=df1[4]
        goal.target_pose.pose.orientation.z=df1[5]
        goal.target_pose.pose.orientation.w = df1[6]#997714974432653
        rospy.loginfo("Sending goal pose "+str(self.goal_cnt+1)+" to Action Server")
        print(df1)
        #rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
        self.client.send_goal(goal, self.done_cb, self.active_cb, self.feedback_cb)
        rospy.spin()

   

if __name__ == '__main__':
    try:
        df = pd.read_csv('my_poses.csv')
        print(df)
        df = df.iloc[:,1:]
        MoveBaseSeq(df)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation finished.")