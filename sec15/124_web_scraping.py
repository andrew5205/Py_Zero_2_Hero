
# basic steps
# 1. import requests, bs4 
# 2. make requests.get() - result = requests.get("URL")
# 3. make soup object - soup = bs4.BeautifulSoup(result.text, "lxml")
# 4. getText between tags - soup.select("TAG")[0].getText()

import requests
import bs4

# https://quotes.toscrape.com/
res = requests.get('https://quotes.toscrape.com/')
# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')


# soup.select('.author')
# author = soup.select('.author')
# print(author)

author = set()

for name in soup.select('.author'):
    author.add(name.text)
# print(author)



# soup.select(.text)
quote = []

for q in soup.select('.text'):
    quote.append(q.text)
# print(quote)



# soup.select('.tag-item')
tags = []

for t in soup.select('tag-item'):
    tags.append(t.text)
# print(tags)



# *********************************************************************************
# when total page is unknown 

url = 'http://quotes.toscrape.com/page/'
page_url = url + str(999999)

result = requests.get(page_url)
soup = bs4.BeautifulSoup(result.text, 'lxml')

# print(result.text)        # check what it look like/ what kinda text it included in outta range page 
                            # "No quotes found!" in this example 
# print("No quotes found!" in result.text)            # True



page_still_valid = True 
authors = set()
page = 1 

while page_still_valid:
    page_url = url+str(page)

    result = requests.get(page_url)
    if "No quotes found!" in result.text:
        break
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    
    for name in soup.select('.author'):
        authors.add(name.text)
        
    page += 1
# print(authors)




