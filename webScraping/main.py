from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", _class="titlelink")
articles_texts = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)


article_upvote = [score.getText() for score in soup.find_all(name="span", _class="score")]

print(articles_texts)
print(articles_links)
print(article_upvote)

