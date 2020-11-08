# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:18:22 2020

@author: Intel
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pandas as pd
import time
import re

#driver = webdriver.Chrome('D:/Intel Files/Desktop/Scraper Project/chromedriver.exe')

link = {
    'NA': 'na.op.gg',
    'KR': 'www.op.gg',
    'EUW': 'eu.op.gg',
}

driver = webdriver.Chrome(executable_path='C:/Users/Jared/Desktop/automated-opgg-coaching/chromedriver.exe')
driver.maximize_window()
#driver.get('https://' + link[region] + 'ranking/ladder')
driver.get('https://na.op.gg/ranking/ladder/')

#https://www.leagueofgraphs.com/rankings/rank-distribution
rank_distribution = {
  'Challenger': '0.011',
  'Grandmaster': '0.027',
  'Master': '0.060',
  'Diamond': '0.78',
  'Platinum': '5.4',
  'Gold': '20',
  'Silver': '32',
  'Bronze': '33',
  'Iron': '7.4'
}

num_players_source = driver.find_element_by_class_name('Text').text
print(num_players_source)
NUM_PLAYERS = re.sub('\D', '', num_players_source)
print(NUM_PLAYERS)
num_users = 10000
visited_pages = []


