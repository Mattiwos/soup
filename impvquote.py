import requests
from bs4 import BeautifulSoup


import random

URL = "https://www.goodreads.com/quotes?page="


def makeRandomPageRequest():
    rint = random.randint(1,100)

    page = requests.get(f"{URL}{rint}")
    if page.status_code == 200:
        pageparsed = BeautifulSoup(page.content,'html.parser')
        #print(pageparsed.prettify())
        
    else:
        print("RE")
        quit()

    #CRUD

    all_quotes = pageparsed.find_all('div',class_='quoteText')
    #, id ="text")
    #.find('div',class_ = "quotes")
    #.find('div', class_='quoteDetails').find('div', class_='quoteText')
    return all_quotes

##print(all_quotes)



def randomQ(list_of_quotes):
   rint = random.randint(1,28)
   return list_of_quotes[rint].get_text()


print(randomQ(makeRandomPageRequest()))
#print(makeRandomPageRequest())