#!/usr/bin/env python

import rospy
from basics.srv import WordCount, WordCountResponse

def word_count(request):
	return WordCountResponse(len(request.word))

rospy.init_node('service_server')
service = rospy.Service('word_count', WordCount, word_count)
rospy.spin()
