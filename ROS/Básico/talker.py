#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import random

def talker():
    velocidade_lin_x = random.randint()
    velocidade_lin_y = random.randint()
    velocidade_lin_z = random.randint()
    velocidade_ang_x = random.randint()
    velocidade_ang_y = random.randint()
    velocidade_ang_z = random.randint()
    pub = rospy.Publisher('vetores', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        velocidade_lin = "velocidade linear: %s" % [velocidade_lin_x, velocidade_lin_y, velocidade_lin_z]
        velocidade_ang = "velocidade angular: %s" % [velocidade_ang_x, velocidade_ang_y, velocidade_ang_z]
        rospy.loginfo(velocidade_lin, velocidade_ang)
        pub.publish(velocidade_lin, velocidade_ang)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
