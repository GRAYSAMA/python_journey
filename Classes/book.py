#Create a Book class with attributes title and author. Instantiate an object of this class
# and print its attributes.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
bgjr = Book("LDR Love Story", "Brett Gray")
print(bgjr.title)
print(bgjr.author)