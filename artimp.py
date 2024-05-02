import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib
import time


url=("https://www.google.com/search?q=astronomy+artist+impression&sca_esv=b7c0b9c8093215b7&rlz=1C1CHBF_en-GBAU1073AU1073&udm=2&prmd=ivsnmbtz&sxsrf=ACQVn0-rpipGMRCe-2vMS0jMSQVSoZJtlw:1713575008045&source=lnt&tbs=isz:l&uds=AMwkrPvYYQ6vD5ewYRAVa2GB4cVKksN4Lch6mcyZEpyXZtUdGrukqS1U06S-KttU1HqEG-BKvysNMTGJVYjs014wgRXx_NfrqNUz2by0GDoc8i2V22E9qZ37-IF3JNL0ysBNKg3IQIO4b1bvSgc7N-myVcgX4H8d74lmG10ZjQ7R4ifFw4oxcPVu9eZhU6kWonS-7zwpM-Bu12y2OcjE2XXmTq6XQKSx3P8DJ14XZCMike08W-LFwQcSd1XpfsfOfBB2dUEE-eZk3Po3VQq_yzoDV2DeKA40X35qfpWyF39BNWJKUcPxCFeDe5VJyHKIebeou_uGgpDT&sa=X&ved=2ahUKEwjc5JmtzM-FAxXFjWMGHYnkCOoQpwV6BAgCEAc&biw=1208&bih=709&dpr=2.19")
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)






SCROLL_PAUSE_TIME = 15

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
M=0
f=open('imagedata/alternatetxt.txt', 'w', encoding='utf-8')
while True:
	N=0
	
	src = []
	alt = []
	imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'YQ4gaf')]")
	for img in imgResults:
		width=int(img.get_attribute('width'))
		if width>50:
			src.append(img.get_attribute('src'))
			alt.append(img.get_attribute('alt'))
			N=N+1

	for i in range(N):
		f.write(alt[i]+"\n")
    
	for i in range(N):    
		urllib.request.urlretrieve(str(src[i]),"imagedata/astroimp{}.jpg".format(M+i))
	M=M+N
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	time.sleep(SCROLL_PAUSE_TIME)
	new_height = driver.execute_script("return document.body.scrollHeight")
   
    
    
    
