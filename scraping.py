# **Web Scraping**

Link of the website for scraping <br>
🔗 http://books.toscrape.com/




### Importing requests and beautifulsoup libraries

from bs4 import BeautifulSoup as bs
import requests

### To scrape the website, define the URL

url = 'http://books.toscrape.com/'   
response = requests.get(url)
response

### This code issues an HTTP GET request to the given URL. It retrieves the HTML data that the server sends back and stores that data in a Python object.

* <Response [200]> means the request succeeded.

If you print the .text attribute of the page, then you'll notice that it looks just like the HTML that you inspected earlier with your browser's developer tools. You successfully fetched the static site content from the Internet! You now have access to the site's HTML from within your Python script.

soup = bs(response.text,'html')
print(soup)

* **soup = bs(...):** This part creates a new BeautifulSoup object, which is a
powerful tool for parsing and navigating HTML content.

* **response.text:** This likely refers to a string containing HTML content that you've obtained from a website. It's probably the text content of a response object retrieved using a library-like request.

* **'html':** This specifies that you're parsing HTML code. BeautifulSoup can handle other markup languages as well, but in this case, it's configured for HTML.

# Extract details of the selected book

---



### .find_all() on a Beautiful Soup object returns an iterable containing all the HTML code displayed on that page

book_tag = soup.find_all('article',class_='product_pod')
book_tag

### To get all the info of the 10th book

book = book_tag[10]
book

### Retrieve the book title from the HTML code, focusing on the selected book(10th book)

title_tag = book.find('a', title = True)['title']
title_tag

### Retrieve the book price from the HTML code, focusing on the selected book(10th book)

price_tag = book.find('p', class_ = 'price_color').text[0:]
price_tag

price_tag = book.find('p', class_ = 'price_color').text[1:]
price_tag

### Retrieve the book rating from the HTML code, focusing on the selected book(10th book)

rating_tag = book.find('p')['class']
rating_tag

rating_tag = book.find('p')['class'][1]
rating_tag

### Retrieve the book link from the HTML code, focusing on the selected book(10th book)

link_tag = f"{ 'https://books.toscrape.com/'}" + book.find('a')['href']
link_tag

### create empty list 

blist = []

### iterate through the books(till the 10th book), extract all information and append it to the list

for books in range(0,11):
  book = book_tag[books]
  title_tag = book.find('a', title = True)['title']
  price_tag = book.find('p', class_ = 'price_color').text[1:]
  rating_tag = book.find('p')['class'][1]
  link_tag = f"{ 'https://books.toscrape.com/'}" + book.find('a')['href']

  blist.append([title_tag, price_tag, rating_tag, link_tag])

print(blist)

### import python library 

import pandas as pd

### create header for each column

columns = ['Title', 'Price', 'Rating', 'Link']
df = pd.DataFrame(blist, columns=columns)
df

### Extract details from all 50 pages 

---



### create empty list 
blist = []

### Loop through all the 50 pages
for page_number in range(1,51):
  url = f'http://books.toscrape.com/catalogue/page-{page_number}.html'
  response = requests.get(url)
  soup = bs(response.text,'html')
  book_tag = soup.find_all('article',class_='product_pod')
  

### append extracted information to the list
  for book in book_tag:
    title_tag = book.find('a', title = True)['title']
    price_tag = book.find('p', class_ = 'price_color').text[1:]
    rating_tag = book.find('p')['class'][1]
    link_tag = f"{ 'https://books.toscrape.com/'}" + book.find('a')['href']

    blist.append([title_tag, price_tag, rating_tag, link_tag])

### create header of each columns and convert list to dataframe

df_final = pd.DataFrame(blist, columns= ['Title', 'Price', 'Rating', 'Link'])
df_final

### Final dataset after scraping website

### save in csv format

df_final.to_csv('scraped.csv', index = False)
print("Data saved")
