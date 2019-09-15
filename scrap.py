# importing the requests library 
import requests 

# defining the api-endpoint 

# your API key here 
API_KEY = "VFca0EG6iykn5iZSkEUnlPADFSpaqD0eO7W0qB79GCbCZVXftu9PM2R3ACti"
data = {"_id":"udemy_review","startUrl":["https://www.udemy.com/the-web-developer-bootcamp/"],"selectors":[{"id":"review-comment-content","type":"SelectorText","parentSelectors":["_root"],"selector":".view-more-container--view-more--25_En p","multiple":True,"regex":"","delay":0}]}

API_ENDPOINT = "https://api.webscraper.io/api/v1/{$data}/api_token=VFca0EG6iykn5iZSkEUnlPADFSpaqD0eO7W0qB79GCbCZVXftu9PM2R3ACti"
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT) 

print(r)
# print("The pastebin URL is:%s"%pastebin_url) 
