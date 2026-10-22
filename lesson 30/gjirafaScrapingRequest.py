import requests

url = ("https://gjirafa50.com/search?q=laptop+gaming")

responses = requests.get(url)

if responses.status_code == 200:
    print(responses.text)
else:
    print(f"Failed to retrieve content from {url} ")