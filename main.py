# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import requests
import time
import re
import datetime
    

def pridobi_podatke():
    browser_options = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images': 2, "profile.default_content_setting_values.notifications" : 2 }
    browser_options.add_experimental_option('prefs', prefs)
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    browser = webdriver.Chrome(PATH, chrome_options=browser_options)

    browser.get('https://www.visitmaribor.si/si/kaj-poceti/dogodki-in-prireditve/vsi-dogodki-in-prireditve/')
    (browser.page_source).encode('utf-8')

    elem_list = browser.find_element(By.CSS_SELECTOR,"div.r-catalogue-list.container.mobile-edge-to-edge")
    items = elem_list.find_elements(By.XPATH, '//a[@data-itemtype= "catEvent"]')

    links = [item.get_attribute("href") for item in items]
    print(links)

    browser.close()

#
#
#

pridobi_podatke()
