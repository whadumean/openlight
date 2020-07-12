import os
import time
from selenium import webdriver
import requests

chrome_options_webduino_light = webdriver.ChromeOptions()
chrome_options_webduino_light.add_argument('--headless')

#開關燈
def light(light_state):
    
    driver = webdriver.Chrome(
        executable_path = chrome_driver_path_for_webduino_light,
        chrome_options = chrome_options_webduino_light
    )

    if light_state == "open":
        driver.get(url_light_open)

    elif light_state == "close":
        driver.get(url_light_close)

    elif light_state == "read":
        driver.get(url_light_read)
        time.sleep(2)
        light_state = driver.find_element_by_tag_name("body").text
        if light_state != "":
            light_state = bool(int(light_state))
        else:
            light_state = False

        return light_state

    elif light_state == "toggle":
        driver.get(url_light_toggle)
        
    time.sleep(2)

    driver.quit()

if __name__ == '__main__':
    chrome_driver_path_for_webduino_light = '../../webdriver/chromedriver.exe'
    url_light_open = 'file:///' + os.path.abspath('./webduino_light_open.html')
    url_light_close = 'file:///' + os.path.abspath('./webduino_light_close.html')
    url_light_read = 'file:///' + os.path.abspath('./webduino_light_read.html')
    url_light_toggle = 'file:///' + os.path.abspath('./webduino_light_toggle.html')


    light("read")

else:
    chrome_driver_path_for_webduino_light = './webdriver/chromedriver.exe'
    url_light_open = 'file:///' + os.path.abspath('./Module/Webduino/webduino_light_open.html')
    url_light_close = 'file:///' + os.path.abspath('./Module/Webduino/webduino_light_close.html')
    url_light_read = 'file:///' + os.path.abspath('./Module/Webduino/webduino_light_read.html')
    url_light_toggle = 'file:///' + os.path.abspath('./Module/Webduino/webduino_light_toggle.html')