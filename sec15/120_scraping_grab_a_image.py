
# <img>
# dowmload




# basic steps
# 1. import requests, bs4 
# 2. make requests.get() - result = requests.get("URL")
# 3. make soup object - soup = bs4.BeautifulSoup(result.text, "lxml")
# 4. getText between tags - soup.select("img")[0]
# 5. computer['src'] - find src tag, by dictionary key, value pair




import requests
import bs4


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

soup.select('img')
# print(soup.select('img')[0])
                    # <img alt="Deep Blue.jpg" data-file-height="601" data-file-width="400" decoding="async" height="331" 
                    # src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg" 
                    # srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/330px-Deep_Blue.jpg 1.5x, 
                    # //upload.wikimedia.org/wikipedia/commons/b/be/Deep_Blue.jpg 2x" width="220"/>


# print(soup.select('.thumbimage')[0])

                    # img alt="" class="thumbimage" data-file-height="600" data-file-width="800" decoding="async" height="165" 
                    # src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png" 
                    # srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/330px-Kasparov_Magath_1985_Hamburg-2.png 1.5x, 
                    # //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/440px-Kasparov_Magath_1985_Hamburg-2.png 2x" width="220"/>



computer = soup.select('.thumbimage')[0]
# print(type(computer))               # <class 'bs4.element.Tag'>

# key, value pair
# print(computer['class'])            # ['thumbimage']
# print(computer['src'])              # //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png


image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")
# print(image_link.content)       # this will be binary 

# mode = write binary
f = open('my_computer_image.jpg', "wb")

f.write(image_link.content)
f.close()





