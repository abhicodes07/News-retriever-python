import requests
import json
from datetime import date 
# Exampler response with all endpoints and headers
# response = requests.get('https://newsapi.org/v2/everything?q=apple&from=2024-08-14&to=2024-08-14&sortBy=popularity&apiKey="YOUR_NEWS_API_KEY')

# https://newsapi.org/v2/top-headlines?q=trump&apiKey=YOUR_NEWS_API_KEY 

class REQUEST: # Making requests
    site = 'https://newsapi.org/' # private get request 
    apikey = '2c0c6a594305428aa1aea424a5e9d745' # private news api key
    # self.endpoint = None
    query = " "
    sortby = " "
    date_from = " "
    date_to = " "
    endpoint = " "
    category = " "
    sources = " "
    country = " "
    language = " "
    domains = " "
    pagesize = " "
    searchin_title = " "
    searchin_description = " "
    searchin_content = " "

    getreq = f"{site}v2/"

    def __init__(self):
        print("-- WELCOME TO THE NEWS RETRIEVER APP -- \n")
        print("--------------------------------------------")
        self.content = Content()

class Content(REQUEST): # Get Content ready
    def __init__(self):
        self.choice_2 = input("-- Please specify the type of news --\n\t1. Everything\n\t2. Top Headlines\n-- Your Choice:  ")
        if self.choice_2 == 1:
            self.every_thing = Everything()
        elif self.choice_2 == 2:
            self.top_headlines = TopHeadlines()

    def getContent(self):
        self.response = requests.get(self.getreq)
        self.content = json.loads(self.response.text) # Contents of news
        # print(self.content)    
        self.articles = self.content["articles"]
        print(self.articles)
    
    def getTitle(self):
        for self.title in self.articles:
            print(self.articles["title"])
            
    def getDescription(self):
        for self.title in self.articles:
            print(self.articles["description"])

class Everything(Content):
    def __init__(self):
        self.endpoint = "everything"
        self.getreq += "everything"

    def query(self):
        """Keywords or phrases to search for in the article title and body"""
        self.query = input("-- Search News: ")
        self.getreq += f"q={self.query}"

    def searchIn(self):
        """ 
        The fields to restrict your q search to.
        The possible options are:
           > title
           > description
           > content
        """
        self.searchIn = int(input("-- Where do you want to search the query in\n\t1. Title\n\t2. Content\n\t3. Description\n\t4. None\n--Your Choice: "))        
        if self.searchIn == 1:
            self.searchin_title = "title"
            self.getreq += f"&searchIn={self.searchin_title}"
        elif self.searchIn == 2:
            self.searchin_content = "content"
            self.getreq += f"&searchIn={self.searchin_content}"
        elif self.searchIn == 3:
            self.searchin_description = "description"
            self.searchIn += f"&searchIn={self.searchin_description}"

    def sources(self):
        pass

    def domains(self):
        """
        A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the search to.
        """
        self.domains = input("-- Enter the domain you want to search it in (eg bbc.co.uk, techcrunch.com, engadget.com): ")
    
    def dateFrom(self):
        """
        A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2024-08-17 or 2024-08-17T15:34:17)
        """
        self.date_from = input("-- Enter the starting date (eg '2024-08-17' or '2024-08-17T16:08:03'): ")

    def to(self):
        """
        A date and optional time for the newest article allowed. This should be in ISO 8601 format (e.g. 2024-08-17 or 2024-08-17T15:34:17)
        """
        self.date_to = input("-- Enter the ending date (eg '2024-08-17' or '2024-08-17T16:08:03'): ")

    def language(self):
        """
        The 2-letter ISO-639-1 code of the language you want to get headlines for. Possible options: ar, de, en, es, fr, he, it, nl, no, pt, ru,sv, ud, zh.
        Default: All language preferred
        """
        self.language = input("Specify the language from these available codes: ar, de, en, es, fr, he, it, nl, no, pt, ru,sv, ud, zh.: ") 

    def sortBy(self):
        """
        The order to sort the articles in. Possible options: relevancy, popularity, publishedAt.
            > relevancy = articles more closely related to q come first.
            > popularity = articles from popular sources and publishers come first.
            > publishedAt = newest articles come first.

            Default: publishedAt
        """
        self.choice_3 = int(input("-- Enter how to do you want to sort the content by from below options\n\t1. Relevancy\n\t2. Popularity\n\t3. Published At\n-- Your choice(1-3): "))
        if self.choice_3 == 1:
            self.sortby = "relevancy"
        elif self.choice_3 == 2:
            self.sortby = "popularity"
        elif self.choice_3 == 3:
            self.sortby = "publishedAt"

    def pageSize(self):
        """
        The number of results to return per page.
        """
        self.pagesize = int(input("Enter the page size you want to see: "))

class TopHeadlines(Everything):
    def __init__(self):
        pass

    def country(self):
        """
        The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options: 
        ae, ar, at, au, be, bg, br, ca, ch, cn, co, cu, cz, de, eg, fr, gb,  gr, 
        hk, hu, id , ie, il, in, it, jp, kr, lt, lv, ma, mx, my, ng, nl, no, nz, 
        ph, pl, pt, ro, rs, ru, sa, se, sg, si, sk, th, tr, tw, ua, us, ve, za
        """
        pass

    def category(self):
        """
        The category you want to get headlines for. Possible options: businessentertainmentgeneralhealthsciencesportstechnology. 
        Note: you can't mix this param with the sources param.
        """
        pass

# main
if __name__ == "__main__":
    user = REQUEST()
    user.newsType()





