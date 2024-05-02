import cv2
import os
import numpy as np


def resize_image(img, size=(256,256)):

	h, w = img.shape[:2]
	c = img.shape[2] if len(img.shape)>2 else 1

	if h == w: 
		return cv2.resize(img, size, cv2.INTER_AREA)
	if h > w:
		dif = h
	else:
		dif= w
	if dif > (size[0]+size[1])//2:
		interpolation = cv2.INTER_AREA
	else:
		interpolation=cv2.INTER_CUBIC

	x_pos = (dif - w)//2
	y_pos = (dif - h)//2

	if len(img.shape) == 2:
		mask = np.zeros((dif, dif), dtype=img.dtype)
		mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]
	else:
		mask = np.zeros((dif, dif, c), dtype=img.dtype)
		mask[y_pos:y_pos+h, x_pos:x_pos+w, :] = img[:h, :w, :]

	return cv2.resize(mask, size, interpolation)


i=0
for filename in os.listdir("./"):
	print(filename)
	if filename.endswith(".jpg"):
		img = cv2.imread(filename)
		if img is None:
			h=0
			w=0
		else:
			h, w = img.shape[:2]
		if h>50 and w>50:
			squared_image=resize_image(img)
			cv2.imwrite("C_"+filename,squared_image)
		i=i+1
