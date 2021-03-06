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
    def __init__(self,  name: str, country: str, birthday: str) -> None:
        self.name = name
        self.country = country
        self.birthday = birthday
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name


class Book:
    count: int = 0
    
    def __init__(self, name: str, year: int, author: Author) -> None:
        self.name = name
        self.year = year
        self.author = author
        Book.count += 1
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    
    
class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list = []
        self.author: list = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
    
    def new_book(self, name: str, year: int, author: Author) -> Book:
        if not isinstance(name, str) or not isinstance(year, int) or not isinstance(author, Author):
            raise TypeError
        book = Book(name, year, author)
        self.books.append(book)
        return book
    
    def group_by_author(self, author: Author) -> list:
        if not isinstance(author, Author):
            raise TypeError
        return [book for book in self.books if book.author.name == author.name]
    
    def group_by_year(self, year: int) -> list:
        if not isinstance(year, int):
            raise TypeError
        return [book for book in self.books if book.year == year]