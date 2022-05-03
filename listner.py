#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    vetor_ang = (velocidade_ang_x**2+ velocidade_ang_y**2+velocidade_ang_z**2)**0.5
    vetor_lin = (velocidade_lin_x**2+ velocidade_lin_y**2+velocidade_lin_z**2)**0.5
    return vetor_ang
    return vetor_lin
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("vetores", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
