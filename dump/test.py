# def upper_case(func):
    
#     def inner():
#         print('inner functions')  
#         text = func()
        
#         print(text.upper())
#     return inner
    
    
# @upper_case
# def test():
    
#     return 'akash'
# test()


# x = lambda a,b : a+b
# print(x(12,23))
# add = lambda x,y:x+y
# print(add(4,5))

# def kwargSample(*ag):
#     ab=ag

  
#     print(ab[2])

# kwargSample(34,'string','nothing',32)
import requests
from bs4 import BeautifulSoup

# URL of the site where the search form is submitted
search_url = 'https://spotifydown.com/'  # Adjust this to the correct action URL

# Search keyword
keyword = 'https://open.spotify.com/track/1PALLCSlHwAI4upY3sMg8u?si=6aaa3e2d34124adb'  # Replace with your desired keyword


data = {
    'searchInput ': keyword,  
  
}
headers = {
    'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://spotifydown.com/',
}


response = requests.post(search_url, data=data,headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('a', href=True)
    print(results)


    for result in results:
        if 'download' in result['href']:
            print(result['href'])
else:
    print("Failed to retrieve the search results.",response.status_code)