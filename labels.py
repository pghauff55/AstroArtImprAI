import cv2
import os
import numpy as np
import random
import tensorflow as tf

labels_train =[]

for i in range(78,216):

	filename="C_astroimp"+str(i)+".jpg"
	print(filename)
	img = cv2.imread(filename)
	#img=cv2.resize(img,(256,64), interpolation= cv2.INTER_LINEAR)
	#img = img.astype(np.float32)
	#img /= 255.
	float_arr=[]
	for m in range(0, 256):
		for n in range(0, 256):
			RGB=img[m,n]
			float_val=float(RGB[0])/255.0
			#print(float_val)
			float_arr.append(float_val)
			float_val=float(RGB[1])/255.0
			#print(float_val)
			float_arr.append(float_val)
			float_val=float(RGB[2])/255.0
			#print(float_val)
			float_arr.append(float_val)

	float_arr=np.array(float_arr).astype(np.float32)
	print(len(float_arr))
	labels_train.append(float_arr)
	
print(len(labels_train))
labels_train=np.array(labels_train)
np.save("labels_train", labels_train)
