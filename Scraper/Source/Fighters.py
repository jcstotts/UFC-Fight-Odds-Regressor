from bs4 import BeautifulSoup
import requests

class Fighter:
    def __init__(self): #Class to contain fighter stats
        self.Name = ''
        self.Nickname = None
        self.Record = (0,0,0)
        self.Height = 0
        self.Reach = 0
        self.Stance = ''
        self.SLpM = 0
        self.DOB = ''
        self.TDAvg = 0
        self.StrAcc = 0
        self.TDAcc = 0
        self.SApM = 0
        self.TDDef = 0
        self.StrDef = 0
        self.SubAvg = 0

def get_fighter_links():
    fighter_links = []

    #Connect to ufcstats.com and create a dictionary for all completed ufc events.
    for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        fighters_URL = 'http://ufcstats.com/statistics/fighters?char=%s&page=all'%letter #Webpage containing all UFC fighters
        page = requests.get(fighters_URL)
        soup = BeautifulSoup(page.content, features='lxml')
        fighters = soup.find_all('tr') #Find all table rows


        for fighter in fighters:
            try:
                if 'fighter-details' in str(fighter.td.a['href']): #Filter out links that do not lead to fighter pages
                    link = fighter.td.a['href']
                    fighter_links.append(link) #Store link for scraping later
            except:
                pass

    return fighter_links

def construct_fighter_objects(fighter_links): #Scrape UFC stats to create fighter classes
    fighters_dict = {}
    num_fighters = 0
    for link in fighter_links:
        num_fighters += 1
        fighter = Fighter()
        fighter_page = requests.get(link)
        fighter_soup = BeautifulSoup(fighter_page.content, features='lxml')
        headers = fighter_soup.find('h2')
        
        first_last = headers.contents[1].text.split()
        for name in first_last:
            fighter.Name += name + ' '
        if 'NC' in headers.contents[3].text:
            fighter.Record = tuple([int(x) for x in headers.contents[3].text.split(':')[1].split('\n')[0].split(' ')[1].split('-')])
        else:
            fighter.Record = tuple([int(x) for x in headers.contents[3].text.split(':')[-1].split('-')])
 

        print(num_fighters, fighter.Name, fighter.Record, vars(fighter))


fighter_links = get_fighter_links()
construct_fighter_objects(fighter_links)