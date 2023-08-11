# Given the Book class, implement the special method __del__ so that the user is informed with the message "Book deleted", displaying it on the screen each time the book is deleted.

class Book():
     def __init__(self, title, author, number_pages):
         self.title = title
         self.author = author
         self.number_pages = number_pages
        
     def __del__(self):
         print(f'Deleted Book')