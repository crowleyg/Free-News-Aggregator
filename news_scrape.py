import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time

#news_scrape scrapes trusted, free news websites for articles given a keyword string. Results are returned in a json file.
#websites searched: npr.org, usatoday.com, reuters.com, thehill.com, time.com, bbc.com
#Input: keyword string
#Output: json file with article title, article url, article date, article source, article text. Grouped by website. 
        
def npr_search(keyword):
    """Searches NPR for articles with the given keyword. 
       Returns a list of dictionaries with article title, article url,
       article date, article source, article text. """
    
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
        try:
            article_dict['date'] = article.find('time')['datetime']
        except:
            article_dict['date'] = 'N/A'
        article_dict['source'] = 'NPR'
        try:
            article_dict['text'] = article.find('p', attrs = {'class': 'teaser'}).text.replace('\u2026', '').replace('\u2014', '')
        except:
            article_dict['text'] = None
        article_list.append(article_dict)
    return article_list

def usatoday_search(keyword):
    """Searches USA Today for articles with the given keyword. 
       Returns a list of dictionaries with article title, article url, 
       article date, article source, article text. """
    
    url = 'https://www.usatoday.com/search/?q=' + keyword
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    content = soup.find('div', attrs = {'class': 'gnt_pr'})
    articles = content.find_all('a', attrs = {'class': 'gnt_se_a'})
    
    article_list = []
    for article in articles:
        a_attributes = article.attrs
        div = article.find('div', attrs = {'class': 'gnt_se_th_by'})
        div_attributes = div.attrs
        substring = div.text
        article_dict = {}
        
        article_dict['title'] = article.text.replace(substring, '')  #removes substring from title
        article_dict['url'] = 'https://www.usatoday.com' + a_attributes['href']
        try:
            article_dict['date'] = div_attributes['data-c-dt']
        except:
            article_dict['date'] = 'N/A'
        article_dict['source'] = 'USA Today'
        article_dict['text'] = a_attributes['data-c-desc']
        article_list.append(article_dict)
    return article_list

def reuters_search(keyword):
    """Searches Reuters for articles with the given keyword. 
       Returns a list of dictionaries with article title, article url, 
       article date, article source, article text. """
       
    url = 'https://www.reuters.com/site-search/?query=' + keyword
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    r = requests.get(url)
    soup = BeautifulSoup(html, 'html5lib')
    content = soup.find('div', attrs = {'class': 'search-results__sectionContainer__34n_c'})
    articles = content.find_all('li', attrs = {'class': 'search-results__item__2oqiX'})

    article_list = []
    for article in articles:
        article_dict = {}
        a_attributes = article.find('a').attrs
        article_dict['title'] = article.find('a').text
        article_dict['url'] = 'https://www.reuters.com' + a_attributes['href']
        article_dict['date'] = article.find('time').text
        article_dict['source'] = 'Reuters'
        article_dict['text'] = None
        article_list.append(article_dict)
    return article_list

def thehill_search(keyword):
    """Searches The Hill for articles with the given keyword. 
       Returns a list of dictionaries with article title, article url, 
       article date, article source, article text. """
        
    url = 'https://thehill.com/?s=' + keyword + '&submit=Search'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    content = soup.find('div', attrs = {'class': 'search__results'})
    #print(content.prettify())
    articles = content.find_all('article', attrs = {'class': 'featured-cards__full'})
    
    article_list = []
    for article in articles:
        article_data = article.find('h1', attrs = {'class': 'featured-cards__full__headline'}).find('a')
        a_attributes = article_data.attrs
        article_dict = {}
        title = article_data.text
        title = title.replace('\n', '')
        title = title.replace('\t', '')
        date = article.find('span', attrs = {'class': 'color-light-gray'}).text
        date = date.replace('\n', '')
        date = date.replace('\t', '')
        article_dict['title'] = title
        article_dict['url'] = a_attributes['href']
        article_dict['date'] = date
        article_dict['source'] = 'The Hill'
        article_dict['text'] = None
        article_list.append(article_dict)
    del article_list[0]
    return article_list

def time_search(keyword):
    """Searches Time for articles with the given keyword. 
       Returns a list of dictionaries with article title, article url, 
       article date, article source, article text. """
        
    url = 'https://time.com/search/?q=' + keyword
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    content = soup.find('div', attrs = {'class': 'margin-16-bottom'})
    articles = content.find_all('article')
    
    article_list = []
    for article in articles:
        article_dict = {}
        title = article.text.replace('\n', '')
        title = title.replace(' | Time', '')
        article_dict['title'] = title.strip()
        article_dict['url'] = article.find('a')['href']
        article_dict['date'] = None
        article_dict['source'] = 'Time'
        article_dict['text'] = None
        article_list.append(article_dict)
    return article_list

def bbc_search(keyword):
    """Searches BBC for articles with the given keyword. 
       Returns a list of dictionaries with article title, article url, 
       article date, article source, article text. """
       
    url = 'https://www.bbc.co.uk/search?q=' + keyword + '&d=HOMEPAGE_GNL'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    content = soup.find('div', attrs = {'class': 'enjd40x0'})
    articles = content.find_all('div', attrs={'class': 'ett16tt0'})
    
    article_list = []
    for article in articles:
        article_dict = {}
        article_dict['title'] = article.find('p', attrs = {'class': 'e1f5wbog5'}).text
        article_dict['url'] = article.find('a', attrs = {'class': 'e1f5wbog1'})['href']
        article_dict['date'] = article.find('span', attrs = {'class': 'ecn1o5v3'}).text
        article_dict['source'] = 'BBC'
        article_dict['text'] = article.find('p', attrs = {'class': 'eq5iqo00'}).text
        article_list.append(article_dict)
    return article_list
    

news_searches = [npr_search, usatoday_search, reuters_search, thehill_search, time_search, bbc_search]
def news_scrape(keyword):
    """Create a json file containing data from news searches"""
    print('News search started')
    search = {'keyword': keyword, 'articles': []}
    for news_search in news_searches:
        search['articles'].extend(news_search(keyword))
    with open('news_search.json', 'w') as outfile:
        json.dump(search, outfile)
    print('News search complete')
    return search

if __name__ == '__main__':
    news_scrape('cars')