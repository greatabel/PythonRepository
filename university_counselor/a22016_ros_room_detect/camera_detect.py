# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import time
import darknet
import rospy
from std_msgs.msg import Int8
import threading
import random
import os
######################

configPath = "./cfg/yolov4-tiny-custom.cfg"
weightPath = "./yolov4-tiny-custom_3000.weights"
metaPath = "./cfg/voc.data"

class_1 = ['桌椅', '餐具', '食物', '人']
class_2 = ['宠物', '床', '沙发', '电视']

class_cj = ['fork', 'kettle', 'spoon', 'tray']
class_cw = ['dog', 'cat', 'parrot','mouse']
class_bed = ['bed']
class_tv = ['tv']
class_people = ['person']
class_sofa = ['l_sofa','s_sofa']
class_food = ['almond', 'apple', 'hamburger', 'noodles']
class_zy = ['chair','desk','r_table']

canteen = ['40', '20', 'C0', 'A0', '60', '50', '30', 'D0', 'E0', 'B0', '70', 'F0']
bedroom = ['04', '18', '14', '1C', '94', '8C', '9C']
drawingroom = ['02', '01', '0A', '82', '03', '09', '81', '8C', '0D', '89', '8D']

change_num = 0

all_audio = ["play ~/ucar_ws/src/mp3/有重复/文本语音\ \(21\).mp3","play ~/ucar_ws/src/mp3/有重复/文本语音\ \(22\).mp3","play ~/ucar_ws/src/mp3/有重复/文本语音\ \(23\).mp3","play ~/ucar_ws/src/mp3/有重复/文本语音\ \(24\).mp3","play ~/ucar_ws/src/mp3/有重复/文本语音\ \(25\).mp3","play ~/ucar_ws/src/mp3/有重复/文本语音\ \(26\).mp3"]

roomtomp3 = {"客厅卧室":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(21\).mp3",
			"客厅餐厅":	"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(22\).mp3",
		    "卧室客厅":	"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(23\).mp3",
			"卧室餐厅":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(24\).mp3",
            "餐厅卧室":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(25\).mp3",
            "餐厅客厅":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(26\).mp3"}

roomtomp4 = {"客厅卧室餐厅":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(21\).mp3",
			"客厅餐厅卧室":	"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(22\).mp3",
		    "卧室客厅餐厅":	"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(23\).mp3",
			"卧室餐厅客厅":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(24\).mp3",
            "餐厅卧室客厅":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(25\).mp3",
            "餐厅客厅卧室":"play ~/ucar_ws/src/mp3/有重复/文本语音\ \(26\).mp3"}

def ID_trans(result):
    ID_1 = 0
    ID_2 = 0
    trans10216 = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D',
                  14: 'E', 15: 'F'}
    for i in result:
        if i in class_1:
            pos_1 = class_1.index(i)
            ID_1 += 2 ** (3 - pos_1)
        elif i in class_2:
            pos_2 = class_2.index(i)
            ID_2 += 2 ** (3 - pos_2)
    ID = str(trans10216[ID_1]) + str(trans10216[ID_2])
    return ID


def DR2BC(detect_result):
    result_t = []
    #print(detect_result)
    for i in detect_result:
        if i in class_cj:
            BClass = '餐具'
        elif i in class_cw:
            BClass = '宠物'
        elif i in class_bed:
            BClass = '床'
        elif i in class_tv:
            BClass = '电视'
        elif i in class_people:
            BClass = '人'
        elif i in class_sofa:
            BClass = '沙发'
        elif i in class_food:
            BClass = '食物'
        elif i in class_zy:
            BClass = '桌椅'
        if BClass not in result_t:
            result_t.append(BClass)
    return result_t

def get_room(ID):
    if ID in canteen:
        return '餐厅'
    elif ID in bedroom:
        return '卧室'
    elif ID in drawingroom:
        return '客厅'
    else:
        return 'error'

def error_correct(ls_room):
	allroom = ['餐厅','卧室','客厅']
	if ls_room.count('error') == 2:
		os.system(all_audio[random.randint(0,len(all_audio)-1)])
	elif ls_room.count('error') == 1:
		broom = ls_room
		broom.remove('error')
		allroom.remove(broom[0])
		replace_room = allroom[random.randint(0,1)]
		allroom.remove(replace_room)
		#ls_room.repalce('error',replace_room)
		lsroom = ls_room
		ls_room = [replace_room if x=='error' else x for x in lsroom]
		ls_room.append(allroom[0])
		final_room = ''.join(ls_room)
		os.system(roomtomp3[final_room])
	else:
		#for i in all_room:
		#	if i not in ls_room:
		#		ls_room.append(i)
		final_room = ''.join(ls_room)
		os.system(roomtomp3[final_room])
		
def callback(msg):
	global change_num
	global room
	change_num = msg.data
	#room = []

def goway():
    rospy.spin()

def getfiles(path):
    filenames = os.listdir(path) #(r'E:\test')
    return filenames

def cvDrawBoxes(detections, img):
    # Colored labels dictionary
    color_dict = {
        "person" : [0, 255, 255]
    }

    for label, confidence, bbox in detections:
        x, y, w, h = (bbox[0],
             bbox[1],
             bbox[2],
             bbox[3])
        name_tag = label
        for name_key, color_val in color_dict.items():
            if name_key == name_tag:
                color = color_val 
                xmin, ymin, xmax, ymax = (
                int(round(x - (w / 2))), int(round(x + (w / 2))), int(round(y - (h / 2))),int(round(y + (h / 2))))
                pt1 = (xmin, ymin)
                pt2 = (xmax, ymax)
                cv2.rectangle(img, pt1, pt2, color, 1)

    return img

network, class_names, class_colors = darknet.load_network(configPath,  metaPath, weightPath, batch_size=1)

rospy.init_node('change_sub')

rate = rospy.Rate(10)

rospy.Subscriber('/detector_sub',Int8,callback)
 
room = []
room_1 = []
room_2 = []
room_3 = []
all_room = []

index = 1

roomB = "/home/ucar/ucar_ws/src/detector/src/darknet-yolov4/roomB/"
roomC = "/home/ucar/ucar_ws/src/detector/src/darknet-yolov4/roomC/"

#cap = cv2.VideoCapture(0)

#_, frame = cap.read()
#rows,cols,channels = frame.shape
#print(rows,cols,channels)
rows = 640
cols = 480
channels = 3

darknet_image = darknet.make_image(cols,rows,3)

spin_thread = threading.Thread(target = goway)
spin_thread.start()

while not rospy.is_shutdown():

	if change_num == 3: #4

		for i in range(2):
			if i == 0:
				room_path = roomB
			elif i == 1:
				room = []
				room_path = roomC
			ph_name = getfiles(room_path)

			for item in ph_name:
				frame = cv2.imread(room_path+item)
				frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
				frame_resized = cv2.resize(frame_rgb,
				#frame_resized = cv2.resize(frame,
						                       (cols, rows),
						                       interpolation=cv2.INTER_LINEAR)
				darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes()) 
				
				###########
				detections = darknet.detect_image(network, class_names, darknet_image, thresh=0.25)
				###########

				#image = cvDrawBoxes(detections, frame)
				
				#darknet.print_detections(detections, False)

				if detections and detections[0][0] not in room and detections[0][1] > str(40):
					#if detections  and detections[0][1] > str(50):
					print(detections[0][0],detections[0][1])
					room.append(detections[0][0])
					#print(room)
					print(detections)
					print(i+1)
						

					if i == 0:
						room_1 = room
						
					if i == 1:
						room_2 = room

			#cv2.imshow("image", frame_resized)
		 
			if cv2.waitKey(1) & 0xFF == ord("q"):
				break

	cv2.destroyAllWindows()

	if room_1 and room_2 and change_num == 4:
		print("room_1:"+str(room_1))
		print("room_2:"+str(room_2))
		for i in range(2):
		    if i == 0:
		        result_ls = room_1
		    elif i == 1:
		        result_ls = room_2

		    result = DR2BC(result_ls)
		    ID = ID_trans(result)
		    room = get_room(ID)
		    all_room.append(room)
		    print(all_room)
		error_correct(all_room)
		break
	rate.sleep()




    


