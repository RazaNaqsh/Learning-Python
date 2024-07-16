import requests
from bs4 import BeautifulSoup


res = requests.get("https://news.ycombinator.com/news")
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

# print(soup.find_all("a"))  # finds all the a tag
# print(soup.find("a"))  # finds the first item
print(soup.find(id="idOfAnyTag"))  # finds the unique ele with the id
print(soup.select(".score"))  # selects with the css selectors
