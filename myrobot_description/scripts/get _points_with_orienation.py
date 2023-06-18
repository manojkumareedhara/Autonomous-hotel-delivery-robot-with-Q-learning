
import rospy
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import _MoveBaseActionGoal

class get_coordinates():
    def __init__(self):
        self.x=x
        self.y=y
        self.z=z
        self.ox=ox
        self.oy=oy
        self.oz=oz
        self.ow=ow
    def callback(self,msg):
        print(msg)
    def get_poses(self):
        rospy.wait_for_message("/move_base_simple/goal",PoseStamped)
        rospy.Subscriber("/move_base_simple/goal",PoseStamped,self.callback)


if __name__=="__main__":
    try:
        co_oordinates=get_coordinates()
        co_oordinates.get_poses()
    except rospy.ROSInterruptException:
        rospy.loginfo("cancelled......................................")
