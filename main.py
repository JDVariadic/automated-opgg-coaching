import high_elo_scraper as hs
import selenium_scraper as ud
import random_users as ru

user_list = hs.scrape_high_elo_data('NA')
ud.get_user_data(user_list, 'NA')