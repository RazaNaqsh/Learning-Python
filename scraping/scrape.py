import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get("https://news.ycombinator.com/news")
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(".titleline a")
subtext = soup.select(".subtext")


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        if idx < len(subtext):  # Ensure we do not go out of bounds
            title = item.getText()
            href = item.get("href", None)
            vote = subtext[idx].select(".score")
            if vote:  # Check if the vote element exists
                points = int(vote[0].getText().replace(" points", ""))
                if points > 100:  # Check if points are greater than 0
                    hn.append({"title": title, "link": href, "votes": points})
    return hn


pprint.pprint(create_custom_hn(links, subtext))
# create_custom_hn(links, subtext)
