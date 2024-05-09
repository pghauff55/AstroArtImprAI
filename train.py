import cv2
import os
import numpy as np
import random
import tensorflow as tf
import time

# get the current time in seconds since the epoch
seconds = time.time()
random.seed(seconds%1000+12)


labels_train=np.load("labels_train.npy")
inputs_train=np.load("input_train.npy")



def make_generator_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(64, use_bias=False, input_shape=(62,)))
    model.add(tf.keras.layers.Dense(128))
    model.add(tf.keras.layers.Dense(512))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Reshape((4, 4, 32)))
   
    model.add(tf.keras.layers.Conv2DTranspose(16, (5, 5), strides=(1, 1), padding='same', use_bias=False))

    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Conv2DTranspose(16, (5, 5), strides=(2, 2), padding='same', use_bias=False))

    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(196608,activation='tanh'))

    return model
    

def eval_model(index,count):
    input_x=np.array(inputs_train[index])
    print(input_x.shape)
    input_x=tf.reshape(input_x,shape=(1,140))
    pred=model.predict(input_x)
    line=[]
    separator=" "
    l=0
    for key in inputs_train[index]:
        if key>0.:
            line.append(keywords[l])
        l=l+1
    title=""
    for kw in line:
       title+=kw+separator
    if len(line)>0:
        print(title)
        img=np.array(pred[0])
        img*=255.
        img=img.astype(np.uint8)
        img=img.reshape(256,256,3)

        img2=np.array(labels_train[index])
        img2*=255.
        img2=img2.astype(np.uint8)
        img2=img2.reshape(256,256,3)
        cv2.imwrite("./images/Astro_"+str(count)+".jpg",img)

        return True
    return False 

def shuffle(inputs_train,labels_train,N_counter):
    counter=0
    while counter<N_counter:
        index1=random.randint(0,len(inputs_train)-1)
        index2=random.randint(0,len(inputs_train)-1)
        temp1=inputs_train[index1]
        temp2=labels_train[index1]
        labels_train[index1]=labels_train[index2]
        labels_train[index2]=temp2
        inputs_train[index1]=inputs_train[index2]
        inputs_train[index2]=temp1
        counter+=1
        #print(inputs_train,labels_train)
        #print(index1,index2)
    return (inputs_train,labels_train)

print(len(inputs_train))
print(len(labels_train))





def make_model():
	inputs = tf.keras.Input(shape=(140,))
	x = tf.keras.layers.Embedding(input_dim=2, output_dim=70, input_length=140)(inputs)
	x = tf.keras.layers.Flatten()(x)
	x = tf.keras.layers.Dense(512)(x)
	x = tf.keras.layers.Dense(1024)(x)

	outputs = tf.keras.layers.Dense(256*256*3,activation="sigmoid")(x)
	model = tf.keras.Model(inputs=inputs, outputs=outputs)
	return model


model=make_model()

model.compile(
    loss=tf.keras.losses.Poisson(),
    optimizer=tf.keras.optimizers.SGD(),
    metrics=[tf.keras.metrics.MeanAbsoluteError()],
)


#(inputs_train,labels_train)=shuffle(inputs_train,labels_train,5*128000)


inputs_train_orig=np.array(inputs_train[0:300])
labels_train_orig=np.array(labels_train[0:300])

#model=tf.keras.models.load_model("./model.keras")


f=open('keywords.txt', 'r', encoding='utf-8')
keywords=f.readlines()
print(keywords)
N=len(inputs_train_orig)
print(N)
K=128000
counter=1
C=20
while counter<10000:
    print("##########################"+repr(counter)+"#############################")
    
    (inputs_train,labels_train)=shuffle(inputs_train_orig,labels_train_orig,3*N)
 
    hist=model.fit(inputs_train, labels_train, epochs=6)
    index=31

    
    

    if counter%C==0:
        while eval_model(index,counter)==False:
           if(index<=140):
                index=index+1
           else:
                break
        
    model.save("./model.keras")
    counter+=1
