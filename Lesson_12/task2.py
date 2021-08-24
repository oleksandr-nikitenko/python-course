"""
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
 for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
"""


class Author:
    def __init__(self,  name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.author = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def new_book(self, name: str, year: int, author: Author) -> object:
        book = Book(name, year, author)
        self.books.append(book)
        return book
    
    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author.name == author.name]
    
    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


class Book:
    count = 0
    
    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.count += 1
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
