from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests

def scrape_high_elo_data(region):
    link = {
        'NA': 'na.op.gg',
        'KR': 'www.op.gg',
        'EUW': 'eu.op.gg',
    }
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://' + link[region] + '/ranking/ladder/')
    html = driver.page_source
    soup = BeautifulSoup(html, features='lxml')
    top_5 = soup.find(id='select_summoner_highest')
    other_top_players = soup.find('table', class_='ranking-table')
    top_players_cell = other_top_players.find_all('tr', class_='ranking-table__row')
    
    top_players_names = top_5.find_all('a', class_='ranking-highest__name')
    other_players_names = [item.find('span') for item in top_players_cell]
    
    top_5_users = [user.get_text() for user in top_players_names]
    top_players_users = [user.get_text() for user in other_players_names]
    top_users_total = top_5_users + top_players_users
    user_dict = {region: top_users_total}
    print(user_dict)
    driver.close()
    return user_dict
    

