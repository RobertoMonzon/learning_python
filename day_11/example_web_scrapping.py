import bs4
import requests

result=requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')
# print(result.text)

soup=bs4.BeautifulSoup(result.text,'lxml')
# print(soup)
# print(soup.select('title'))
# print(soup.select('h1'))
# print(soup.select('a'))
# print(len(soup.select('a')))
# print(soup.select('title')[0].getText())
side=soup.select('.content p')
for p in side:
    print(p.getText())