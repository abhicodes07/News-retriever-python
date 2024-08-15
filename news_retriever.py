import requests

# Exampler response with all endpoints and headers
response = requests.get('https://newsapi.org/v2/everything?q=apple&from=2024-08-14&to=2024-08-14&sortBy=popularity&apiKey=2c0c6a594305428aa1aea424a5e9d745')
print(response.text)






