import requests
from bs4 import BeautifulSoup
import random

URL = "http://quotes.toscrape.com/page/"


def makeRandomPageRequest():
    rint = random.randint(1,10)

    page = requests.get(f"{URL}{rint}")
    if page.status_code == 200:
        pageparsed = BeautifulSoup(page.content,'html.parser')
        #print(pageparsed.prettify())
        
    else:
        print("RE")
        quit()

    #CRUD

    all_quotes = pageparsed.find_all('span', class_='text')
    return all_quotes

##print(all_quotes)



def randomQ(list_of_quotes):
   rint = random.randint(0,9)
   return list_of_quotes[rint].get_text()


print(randomQ(makeRandomPageRequest()))