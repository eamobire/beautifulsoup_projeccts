from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name='a', class_='storylink')
all_article_text = []
all_article_links = []

for articles_tag in articles:
    articles_text = articles_tag.getText()
    all_article_text.append(articles_text)
    articles_link = articles_tag.get('href')
    all_article_links.append(articles_link)

all_up_votes = [int(vote.getText().split()[0]) for vote in soup.find_all(name='span', class_='score')]

# print(all_article_text)
# print(all_article_links)
# print(all_up_votes)
max_votes = all_up_votes.index(max(all_up_votes))

print(f"{all_article_text[max_votes]}, {all_article_links[max_votes]}, {all_up_votes[max_votes]}")

# for tags in article_tags:
#     print(tags.getText())


# with open("index.html") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# anchor_tags = soup.find_all(name="a")
# # print(anchor_tags)
#
# for tags in anchor_tags:
#     # print(tags.getText())
#     print(tags.get("href"))
