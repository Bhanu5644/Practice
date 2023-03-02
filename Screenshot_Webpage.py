from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

serv_obj=Service("C:/Users/BHANU/Documents/geko.exe")
driver=webdriver.Chrome(service=serv_obj)
time.sleep(5)
driver.get("https://www.google.com/")
driver.save_screenshot("C:/Users/BHANU/PycharmProjects/Practice/ScreenShot/bhanu.png")
driver.maximize_window()
driver.close()

