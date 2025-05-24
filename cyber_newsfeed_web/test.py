import requests

response = requests.get('https://thehackernews.com/feeds/posts/default')
print(response.status_code)
print(response.text[:500])
