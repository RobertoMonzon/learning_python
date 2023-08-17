import bs4
import requests
url_base='http://books.toscrape.com/catalogue/page-{}.html'

# print(url_base.format('15'))

# for n in range(1,51):
#     print(url_base.format(n))

# results= requests.get(url_base.format('1'))
# soup=bs4.BeautifulSoup(results.text,'lxml')
# books=(soup.select('.product_pod'))

# # example=books[0].select('.star-rating.Three')
# example=books[0].select('a')[1]['title']
# print(example)


title_rating_4_and_5=[]
for page in range(1,51):

    url_page=url_base.format(page)
    result= requests.get(url_page)
    soup=bs4.BeautifulSoup(result.text, 'lxml')

    books=soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) !=0:

            title= book.select('a')[1]['title']
            title_rating_4_and_5.append(title)


for t in title_rating_4_and_5:
    print(t)
