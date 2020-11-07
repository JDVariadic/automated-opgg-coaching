# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:18:22 2020

@author: Intel
"""


driver = webdriver.Chrome('D:/Intel Files/Desktop/Scraper Project/chromedriver.exe')
driver.maximize_window()
driver.get('https://' + link[region] + '/summoner/userName=' + user)