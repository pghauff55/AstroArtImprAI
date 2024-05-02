import cv2
import os
import numpy as np
import random
import tensorflow as tf
import random
import time

seconds = time.time()
random.seed(seconds%1000+12)
inputs_train=np.load("imagedata2/input_train.npy")
model=tf.keras.models.load_model("imagedata2/model1.keras")
inputs_train=np.array(inputs_train)

f=open('imagedata2/keywords.txt', 'r', encoding='utf-8')
keywords=f.readlines()
print(keywords)
N=len(inputs_train)
K=128000
counter=1
C=10
while counter<1000:
    print("##########################"+repr(counter)+"#############################")
    
    index1=random.randint(0,61)
    index2=random.randint(0,61)
    index3=random.randint(0,61)
    inputs_x=np.zeros(62)
    inputs_x[index1]=1.0
    inputs_x[index2]=1.0
    inputs_x[index3]=1.0
    
    
    input_x=np.array(inputs_x)
    print(input_x.shape)
    input_x=tf.reshape(input_x,shape=(1,62))
    pred=model.predict(input_x)
    line=[]
    separator=" "
    l=0
    for key in inputs_x:
        if key>0.:
            line.append(keywords[l])
        l=l+1
    title=""
    for kw in line:
       title+=kw+separator
    print(title)

    img=np.array(pred[0])
    img*=255.
    img=img.astype(np.uint8)
    img=img.reshape(256,256,3)
    
    
    
    cv2.imshow(title,img)
    cv2.waitKey(50000) 
    cv2.destroyAllWindows()
    

    counter+=1



