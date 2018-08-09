#coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

#打开网址
browser.get("http://www.baidu.com")
#为控件输入值
browser.find_element_by_id("kw").send_keys("selenium")
#点击按钮
browser.find_element_by_id("su").click()
time.sleep(3)
#关闭浏览器
browser.close()