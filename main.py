import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
# print(res.text) #prints the entire 'elements' tab of dev tools.
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
# print(soup) #gives html for entire page.
# print(soup.find_all("div"))
# print(soup.find_all("a"))

# print(soup("a"))  # finds the first
# print(soup.select("a")) #CSS select
# print(soup.select(".score")) #list of all spans with a class of score


links = soup.select(".storylink")
subtext = soup.select(".subtext")

links2 = soup2.select(".storylink")
subtext2 = soup2.select(".subtext")
# print(links[0], votes[0])

all_links = links + links2
all_subtext = subtext + subtext2


def sort_stories_by_votes(hndict):
    return sorted(hndict, key=lambda k: k["vote"], reverse=True)


def create_custom_hackernews(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.get_text()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")

        if len(vote):
            points = int(vote[0].get_text().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "vote": points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hackernews(all_links, all_subtext))
