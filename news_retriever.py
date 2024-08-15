import requests

# Exampler response with all endpoints and headers
# response = requests.get('https://newsapi.org/v2/everything?q=apple&from=2024-08-14&to=2024-08-14&sortBy=popularity&apiKey="YOUR_NEWS_API_KEY')

class REQUEST: # Making requests
    site = 'https://newsapi.org/' # private get request 
    apikey = 'YOUR_NEWS_API_KEY' # private news api key
    # self.endpoint = None
    getreq = " "

    def __init__(self):
        print("-- WELCOME TO THE NEWS RETRIEVER APP -- ")
        print("-- Please select from the below options! --")
        print("\n\t1. View news based on endpoints\n\t2. Search using Keyword or Phrase\n\t3. Search Publisher\n\t4. Search in different Language\n\t5. Search Headlines\n")
        self.choice_1 = int(input("Your choice (1-6): "))
        
    def newsType(self):
        if self.choice_1 == 1:
            test = Endpoint()
            test.endPoint()

class Endpoint(REQUEST): # Retrieve news with title
    everything = '/v2/everything'
    headlines = '/v2/top-headlines'

    def __init__(self):
        self.choice_2 = int(input("-- Select from below types of headlines/endpoint: \n\t1. Everything\n\t2. Top Headlines\n Your choice (1-2): "))
    
    def endPoint(self):
        if self.choice_2 == 1:
            self.topHeadlines()
        elif self.choice_2 == 2:
            self.everyThing()

    def everyThing(self):
        self.getreq = self.site + self.everything + '?q=tesla&from=2024-07-15&sortBy=publishedAt&apiKey=' + self.apikey 
        self.response = requests.get(self.getreq)   
        print(self.response.text)

    def topHeadlines(self):   
        self.getreq = self.site + self.headlines + '?q=tesla&from=2024-07-15&sortBy=publishedAt&apiKey=' + self.apikey 
        self.response = requests.get(self.getreq)
        print(self.response.text)

class Query(REQUEST):
    pass

class Publisher(REQUEST):
    pass

class Language(REQUEST):
    pass

class Date(REQUEST):
    pass

class Headlines(REQUEST):
    pass

# main
if __name__ == "__main__":
    user = REQUEST()
    user.newsType()





