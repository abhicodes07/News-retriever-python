import requests

# Exampler response with all endpoints and headers
# response = requests.get('https://newsapi.org/v2/everything?q=apple&from=2024-08-14&to=2024-08-14&sortBy=popularity&apiKey=2c0c6a594305428aa1aea424a5e9d745')

class REQUEST: # Making requests
    def __init__(self):
        self.getreq = 'https://newsapi.org/' # private get request 
        self.apikey = '2c0c6a594305428aa1aea424a5e9d745' # private news api key
        # self.endpoint = None
    def welcome(self):
        pass

class Endpoint(REQUEST): # Retrieve news with title
    def __init__(self):
        super().__init__()
        self.choice = int(input("Select from below types of headlines: \n\t1. Everything\n\t2. Top Headlines\n Your choice (1-2): "))
     
    def endpoint(self):
        if self.choice == 1:
            self.type = '/v2/everything'
        elif self.choice == 2:
            self.type = '/v2/top-headlines'

        self.req = self.getreq + self.type + '?q=tesla&from=2024-07-15&sortBy=publishedAt&apiKey=' + self.apikey 
        self.response = requests.get(self.req)
        # print(self.test)
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
    test = Endpoint()
    test.endpoint()





