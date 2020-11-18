# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:09:36 2020

@author: Jared
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.op.gg/ranking/ladder/')
page = requests.get('http://google.com')
html = driver.page_source
soup = BeautifulSoup(html)
print(soup.prettify())
#print(soup.prettify())
