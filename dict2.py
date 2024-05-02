import os
import numpy as np
import random

def ExtractAlphanumeric(InputString):
    from string import ascii_letters, digits
    return "".join([ch for ch in InputString if ch in (ascii_letters + digits)])


common_words=["from","the","with","and","artist","impression","artists","how","art","our","are","what","could","may","news","around","image","most","mullum","like","images","stock"]
def commonword(inputstr):
	for cw in common_words:
		if inputstr==cw:
			 return True
	return False

Lines=[]
with open('alternatetxt.txt', 'r', encoding='utf-8') as f:
	Lines=f.readlines()
print(len(Lines))
KeyWords=[]
for line in Lines:
	keywords=line.split(' ',-1)
	for keyword in keywords:
		k=ExtractAlphanumeric(keyword).lower()
		if len(k)>2 and not commonword(k):
			KeyWords.append(k)
KeyWords2=list(dict.fromkeys(KeyWords))
mydict={}
mydict2={}
input_train=[]
i=0




for k in KeyWords:
	k=ExtractAlphanumeric(k).lower()
	if k in mydict2:
		mydict2[k]=mydict2[k]+1
	else:
		mydict2[k]=0
	

f=open('keywords.txt', 'w', encoding='utf-8')
i=0
for k in KeyWords2:
	k=ExtractAlphanumeric(k).lower()
	if mydict2[k]>4:
		mydict[k]=i
		print(k)
		f.write(k+"\n")
		i=i+1
f.close()
print("Number of dictionary entries with more than four entries ",format(i))
j=0
for line in Lines:
	if j>215:
		break
	if j>=78:
		index_list=np.zeros(62)
		keywords=line.split(' ',-1)
		for keyword in keywords:
			keyword=ExtractAlphanumeric(keyword).lower()
			if keyword in mydict:
				index_list[mydict[keyword]]=1.0
		#print(index_list)
		input_train.append(index_list)
	j=j+1
print(len(input_train))
np.save("input_train", input_train)
