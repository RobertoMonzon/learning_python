import bs4
import requests

result=requests.get('https://www.escueladirecta.com/courses')
soup=bs4.BeautifulSoup(result.text,'lxml')
# images=soup.select('img')
# for i in images:
#     print(i)

# images=soup.select('.course-box-image')
# for i in images:
#     print(i)

images=soup.select('.course-box-image')[0]['src']
print(images)

images_1=requests.get(images)
# print(images_1.content)
f=open('mi_image.jpg','wb')
f.write(images_1.content)
f.close()