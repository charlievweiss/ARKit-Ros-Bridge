#!/usr/bin/env python

from arkit_streamer.srv import *
import rospy

def get_phone_type(req):
    return "iPhone"

def phone_type_server():
    rospy.init_node('phone_type_server')
    s = rospy.Service('phone_type', phone, get_phone_type)
    rospy.spin()

if __name__ == "__main__":
    phone_type_server()
