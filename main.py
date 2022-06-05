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
    for site_url in links:
        browser.get(site_url)
        (browser.page_source).encode('utf-8')
        vsebina = browser.find_element(By.CSS_SELECTOR,"div.col-lg-7, div.col-lg-6")
        naslov = vsebina.find_element(By.XPATH, '//h2[@class="heading__title"]').text
        try:
            opis = vsebina.find_element(By.TAG_NAME, "p").text
        except:
            opis = "NULL"
        try:
            image = browser.find_element(By.CSS_SELECTOR, 'div.col-lg-5.event-image')
            slika_url = image.find_element(By.TAG_NAME, "img")
            url = slika_url.get_attribute("src")
        except:
            image = "NULL"
            slika_url = "NULL"
            url="NULL"   
        podatki = vsebina.find_elements(By.XPATH, '//div[@class="featured-content__text"]')
        podatki_array = []
        for p in podatki:
            podatki_array.append(p.text)

        #
        #
        #
        
        print(podatki_array)

    browser.close()

#
#
#

pridobi_podatke()
