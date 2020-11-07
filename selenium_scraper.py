# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:49:46 2020

@author: Intel
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pandas as pd
import time

def click_element(xpath):
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()
    
def click_element_by_desc_name(desc_name):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, desc_name))
    )
    element.click()
    
def click_ad(xpath):
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()

def find_stat(css, context):
    return context.find_element_by_css_selector(css).text

def get_random_users(num_users, driver):
    random_users = []
    return random_users
    
#ADVERTISEMENT XPATH //*[@id="assets"]/polygon
stats = []
users = [('HULKSMASH1337', 'NA')]
num_matches = 1
driver = webdriver.Chrome('D:/Intel Files/Desktop/Scraper Project/chromedriver.exe')
driver.maximize_window()
link = {
    'NA': 'na.op.gg',
    'KR': 'www.op.gg',
    'EUW': 'eu.op.gg',
}
games_per_tab = 20
press_read_more = math.floor(num_matches / games_per_tab)
for user, region in users:
    driver.get('https://' + link[region] + '/summoner/userName=' + user)
    
    for i in range(press_read_more):
        #click_ad('//*[@id="assets"]/polygon')
        click_element_by_desc_name('Show More')
        time.sleep(1)
    
    time.sleep(1)
    user_matches = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'GameItemWrap')))

    for match in range(num_matches):
        current_match = ''
        try:
            current_match = user_matches[match]
        except:
            print('Match cannot be found')
            
        match_id_container = current_match.find_elements_by_class_name('GameItem')
        current_game_id = ''
        
        for datum in match_id_container:
            current_game_id = datum.get_attribute('data-game-id')

        tier_average = 'None'
        try:
            tier_average = find_stat('div[class="MMR"] b', current_match)
        except:
            tier_average = 'None'
            
        game_type = current_match.find_element_by_class_name('GameType').text
        match_status = find_stat('div[class="GameResult"]', current_match)
        match_duration = find_stat('div[class="GameLength"]', current_match)
        champion_used = find_stat('div[class="ChampionName"] a', current_match)
        kda = find_stat('div[class="KDA"]', current_match).split('\n')[0]
        user_level = find_stat('div[class="Level"]', current_match)
        kill_participation = current_match.find_element_by_class_name('CKRate').text
        total_cs = find_stat('div[class="CS"]', current_match)
        control_wards_bought = 0
        try: 
            control_wards_bought = current_match.find_element_by_class_name('Trinket').text
        except:
            control_wards_bought = 0
        
        spell_list = []
        spells = current_match.find_elements_by_class_name('Spell')
        
        for spell in spells:
            spell_list.append(spell.find_element_by_tag_name('img').get_attribute('alt'))
            
        stats.append({
                'Game Type': game_type,
                'Match ID': current_game_id,
                'Tier Average': tier_average,
                'user': user,
                'Match Status': match_status,
                'Match Duration': match_duration, 
                'Champion Used': champion_used, 
                'K/D/A': kda,
                'Kill Participation': kill_participation,
                'Total CS': total_cs,
                'Control Wards Bought': control_wards_bought,
                'User Level': user_level,
                'D_spell': spell_list[0],
                'F_spell': spell_list[1]
        })
        
        
    
    df = pd.DataFrame(stats)
    df.to_csv('league_data.csv')
    


    


