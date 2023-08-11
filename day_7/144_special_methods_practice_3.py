# Given the Book class, implement the special method __len__ so that each time the len() function is executed on it, it returns the number of pages as an integer.

class Book():
     def __init__(self, title, author, number_pages):
         self.title = title
         self.author = author
         self.number_pages = number_pages

     def __len__(self):
         return self.number_pages