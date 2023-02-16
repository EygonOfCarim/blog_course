from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.findAll(name="a") #all tags A

for tag in all_anchor_tags:
    print(tag.getText())

heading = soup.find(name="h1", id="name")
print(heading)

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
