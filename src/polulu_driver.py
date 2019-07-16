#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from dual_g2_hpmd_rpi import motors, MAX_SPEED

def move():

	sub = rospy.Subscriber("cmd_vel", Twist, update_signals)
	rospy.spin()

def update_signals(incoming_twist):
	rospy.loginfo("Command Recieved!")
	arcade_drive(incoming_twist.angular.z, incoming_twist.angular.x)

def arcade_drive(left, forward):
	send_motor_pwr(forward - left, forward + left);

def send_motor_pwr(left, right):
	motors.enable()
	motors.setSpeeds(int(left * float(MAX_SPEED)), int(right * float(MAX_SPEED)))

if __name__ == "__main__:"
	rospy.init_node("polulu_driver")
	move()
	

