from bs4 import BeautifulSoup
import requests

def event_data():
    events_dictionary = {}

    #Connect to ufcstats.com and create a dictionary for all completed ufc events.
    events_URL = 'http://ufcstats.com/statistics/events/completed?page=all' #Webpage containing all completed UFC events
    page = requests.get(events_URL)
    soup = BeautifulSoup(page.content, features='lxml')
    events = soup.find_all('a', href = True)

    for event in events:
        if 'event-details' in str(event['href']): #Filter out links that do not lead to events
            #print(event['href'], event.text)
            events_dictionary[event.text] = event['href']

    return events_dictionary