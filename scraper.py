from bs4 import BeautifulSoup
import requests
import os
import lxml

def scraper():
    
    list_of_urls = []
    
    # Import urls from text file
    urls = open("urls.txt", "r")
    
    # Add urls to our list of addresses to scrape
    for lines in urls:
        list_of_urls.append(lines)
    
    # Scrape the <p> content from each url and save to a .txt file
    for u in list_of_urls:
        r = requests.get(u)
        soup = BeautifulSoup(r.content, 'lxml')
        paragraphs = soup.find_all('p')
        
        title = soup.find_all('h1')[0].get_text()
        filename = "".join([title, '.', 'txt'])
        
        for p in paragraphs:
            p.get_text() 
            with open(filename, 'a') as f:
                f.write(p.get_text().encode('utf-8'))
      

scraper()
