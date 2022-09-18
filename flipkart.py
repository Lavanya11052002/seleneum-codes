import pandas as pb
import selenium
import os
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
def flipkart(a):
    dl="F:\\seli\\driver\\chromedriver.exe" # driver path
    os.environ["webdriver.chrome.driver"]=dl
    d=wd.Chrome(dl)
    d.get(a)
    a=d.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]').text
    print(a)
print("enter prodect path :")
a=input()
flipkart(a)