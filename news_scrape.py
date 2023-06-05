import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import datetime
import time

#news_scrape scrapes trusted, free news websites for articles given a keyword string. Results are returned in a json file.
#websites searched: npr.org, usatoday.com, newsweek.com, reuters.com, thehill.com, time.com, bbc.com
#Input: keyword string
#Output: json file with article title, article url, article date, article source, article text. Grouped by website. 

def news_scrape(keyword):
    pass
def npr_search(keyword):
    """Searches NPR for articles with the given keyword. Returns a list of dictionaries with article title, article url, article date, article source, article text. """
    
    url = 'https://www.npr.org/search/?query=' + keyword
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    r = requests.get(url)
    soup = BeautifulSoup(html, 'html5lib')
    content = soup.find('main', attrs = {'aria-label': 'main content'})
    articles = content.find_all('article')
    
    article_list = []
    for article in articles:
        article_dict = {}
        article_dict['title'] = article.find('h2').text
        article_dict['url'] = 'https://www.npr.org' + article.find('h2').find('a')['href']
        article_dict['date'] = article.find('time')['datetime']
        article_dict['source'] = 'NPR'
        article_dict['text'] = article.find('p', attrs = {'class': 'teaser'}).text
        article_list.append(article_dict)
    return article_list

if __name__ == '__main__':
    print(npr_search('president'))
    