class Books:
    def __init__(self, title:str, author:str, publication_year:str, type:str):
        self.title = title
        self.author = author
        self.publication_year= publication_year
        self.type= type
        
        
    def show_info(self):
        print(f'Title: {self.title}\n'
              f'Author: {self.author}\n'
              f'Publication year: {self.publication_year}\n'
              f'Type: {self.type}\n')
                      
               
class Library:
    def __init__(self):
        self.book_list = []          
        
    def add_book(self, book):
        if any(b.title.lower() == book.title.lower()  for b in self.book_list):
            print(f"'{book.title} kütüphanede mevcut...'\n")
        else:      
            self.book_list.append(book)
            print(f"'{book.title}' kütüphaneye eklendi.\n")
        
    def list_books(self):
        for book in self.book_list:
           book.show_info()
          
            
book1 = Books("Simyacı", "Paulo Coelho", 1988, "Novel")
book2 = Books("Suç ve Ceza", "Fyodor Dostoyevski", 1866, "Novel")
book3 = Books("Suç ve Ceza", "Fyodor Dostoyevski", 1866, "Novel")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()

library.add_book(book3)
library.list_books()

