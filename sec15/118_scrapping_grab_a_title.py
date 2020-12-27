
# basic steps
# 1. import requests, bs4 
# 2. make requests.get() - result = requests.get("URL")
# 3. make soup object - soup = bs4.BeautifulSoup(result.text, "lxml")
# 4. getText between tags - soup.select("TAG")[0].getText()




import requests
import bs4


# requests.get("URL")
result = requests.get("http://example.com/")

print(type(result))             # <class 'requests.models.Response'>

print(result.text)
# <!doctype html>
# <html>
# <head>
#     <title>Example Domain</title>

#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
#     }
#     div {
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }
#     a:link, a:visited {
#         color: #38488f;
#         text-decoration: none;
#     }
#     @media (max-width: 700px) {
#         div {
#             margin: 0 auto;
#             width: auto;
#         }
#     }
#     </style>    
# </head>

# <body>
# <div>
#     <h1>Example Domain</h1>
#     <p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>
#     <p><a href="https://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>


import bs4
# soup = bs4.BeautifulSoup(result.text, "lxml") - to make soup
soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup) - will print same as result.text


# soup.select("TAG")
print(soup.select("title"))             # [<title>Example Domain</title>] - list
print(soup.select("h1"))                # [<h1>Example Domain</h1>]
print(soup.select("p"))
                                        # [<p>This domain is for use in illustrative examples in documents. You may use this
                                        #     domain in literature without prior coordination or asking for permission.</p>, <p><a href="https://www.iana.org/domains/example">More information...</a></p>]



# print(soup.select("title"))             # [<title>Example Domain</title>] - list
# bs4.getText() - between tag
print(soup.select("title")[0].getText())        # Example Domain









