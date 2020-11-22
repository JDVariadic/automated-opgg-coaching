from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
import math
import pandas as pd
#driver = webdriver.Chrome('D:/Intel Files/Desktop/Scraper Project/chromedriver.exe')
#C:/Users/Jared/Desktop/automated-opgg-coaching/chromedriver.exe
def get_random_users():
    link = {
        'NA': 'na.op.gg',
        'KR': 'www.op.gg',
        'EUW': 'eu.op.gg',
    }
    
    #D:/Intel Files/Desktop/Scraper Project/chromedriver.exe
    driver = webdriver.Chrome('chromedriver.exe')
    #driver.maximize_window()
    #driver.get('https://' + link[region] + 'ranking/ladder')
    driver.get('https://na.op.gg/ranking/ladder/')
    
    #https://www.leagueofgraphs.com/rankings/rank-distribution
    
    #Expressed as Percentage. (e.g Challenger is actually 0.011% of the playerbase)
    rank_distribution = {
      'Challenger': 0.011,
      'Grandmaster': 0.027,
      'Master': 0.060,
      'Diamond': 0.78,
      'Platinum': 5.4,
      'Gold': 20,
      'Silver': 32,
      'Bronze': 33,
      'Iron': 7.4
    }
    rank_list = []
    value_list = []
    num_players_source = driver.find_element_by_class_name('Text').text
    NUM_PLAYERS = int(re.sub('\D', '', num_players_source))
    PLAYERS_PER_PAGE = 100
    num_users = 1000
    rank_page_boundaries = {}
    
    #Upper Bound of search for each rank distribution
    num_pages = math.ceil(NUM_PLAYERS / 100)
    
    lower_bound = 0
    for rank, value in rank_distribution.items():
        upper_bound = math.ceil(lower_bound + num_pages * (rank_distribution[rank] / 100)) + 1
        rank_page_boundaries[rank] = {'Lower Bound': lower_bound, 'Upper Bound': upper_bound }
        lower_bound = upper_bound
    
    for key, value in rank_page_boundaries.items():
        print(key, value)
        
    for key, value in rank_distribution.items():
        rank_list.append(key)
        value_list.append(value)
        
    random_items = random.choices(rank_list, weights=value_list, k=num_users)
    print('random_items len ', len(random_items))
    '''
    if 'Challenger' in random_items:
        print('Challenger appeared')
    else:
        print('No challenger player found')
    '''
    
    num_players_per_rank = {}
    random_page_selection = []
    players = {}
    for rank in rank_distribution.keys():
        num_players_per_rank[rank] = random_items.count(rank)
        players[rank] = []
    '''
    for arr in num_players_per_rank:
        for key in arr:
            print(key, arr[key])
    '''
        
    
    
    for key, value in num_players_per_rank.items():
        while len(players[key]) < value:
            #Get a fresh list of users
            driver.get('https://na.op.gg/ranking/ladder/page=' + str(random.randint(rank_page_boundaries[key]['Lower Bound'], rank_page_boundaries[key]['Upper Bound'])))
            user_list = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ranking-table__row')))
            #Keep appending usernames in a list until all 100 have been passed through
            for item in user_list:
                if len(players[key]) < value:
                    summoner = item.find_element_by_class_name('select_summoner')
                    summoner_name = summoner.find_element_by_tag_name('span').text
                    players[key].append(summoner_name)
                else: 
                    break
    
    final_players = []
    
    for key, value in players.items():
        print(value)
        for player in value:
            final_players.append({'Player': player, 'Rank': rank})
    driver.close()
        
    return final_players
    
    '''
    df = pd.DataFrame(final_players)
    df.to_csv('players.csv')
    '''
    
    '''
    num_player = num_players_per_rank[key]
    for i in range(num_player):
        players[rank].append('testing')
    '''
    
    '''
    for rank in random_items:
        random_value = random.randint(rank_page_boundaries[rank]['Lower Bound'], rank_page_boundaries[rank]['Upper Bound'])
        if random_value not in random_page_selection:
            random_page_selection.append(random_value)
    '''      
    
            
    '''
    for rank in rank_distribution:
        rank_page_boundaries[rank].append({'Upper Bound': })
    '''  


