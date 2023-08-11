# Given the Book class, implement the special method __str__ so that each time the object is printed, 
# it returns '"{title}", by {author}' (note: the title must be enclosed in double quotes).
class Book():
     def __init__(self, title, author, number_pages):
         self.title = title
         self.author = author
         self.number_pages = number_pages
 
     def __str__(self):
         return (f'"{self.title}", from {self.author}')
     
it=Book("It","Stephen King",200)

print(it.title)
print(str(it))