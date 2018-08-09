#coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
url = "http://www.baidu.com"

browser.get(url)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()


time.sleep(3)
browser.back() #返回
time.sleep(2)
browser.forward() #前进
#browser.minimize_window() #最小化窗口
#time.sleep(2)
#browser.maximize_window() #最大化窗口
#browser.set_window_size(400,200) #设置浏览器宽高

browser.implicitly_wait(10)
browser.close()