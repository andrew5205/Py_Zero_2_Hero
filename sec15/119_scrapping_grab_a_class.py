
# soup.select('div')
# soup.select('#_ID')
# soup.select('._class')
# soup.select('div span')
# soup.select('div>span') - any elements named span directly within a div element, with nothing in between 




# basic steps
# 1. import requests, bs4 
# 2. make requests.get() - result = requests.get("URL")
# 3. make soup object - soup = bs4.BeautifulSoup(result.text, "lxml")
# 4. getText between tags - soup.select("TAG")[0].getText()

import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

soup.select(".toctext")
# print(soup.select(".toctext"))


for e in soup.select('.toctext'):
    print(e.getText())
                        # Early life and education
                        # Career
                        # World War II
                        # UNIVAC
                        # COBOL
                        # Standards
                        # Retirement
                        # Post-retirement
                        # Anecdotes
                        # Death
                        # Dates of rank
                        # Awards and honors
                        # Military awards
                        # Other awards
                        # Legacy
                        # Places
                        # Programs
                        # In popular culture
                        # Grace Hopper Celebration of Women in Computing
                        # See also
                        # Notes
                        # Obituary notices
                        # References
                        # Further reading
    print(e.text)
                        # Early life and education
                        # Career
                        # World War II
                        # UNIVAC
                        # COBOL
                        # Standards
                        # Retirement
                        # Post-retirement
                        # Anecdotes
                        # Death
                        # Dates of rank
                        # Awards and honors
                        # Military awards
                        # Other awards
                        # Legacy
                        # Places
                        # Programs
                        # In popular culture
                        # Grace Hopper Celebration of Women in Computing
                        # See also
                        # Notes
                        # Obituary notices
                        # References
                        # Further reading
                        # External links





