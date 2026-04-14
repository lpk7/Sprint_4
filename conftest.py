import pytest
import data
from main import BooksCollector


@pytest.fixture(scope="function")
def books_collector():
    collector = BooksCollector()
    return collector


@pytest.fixture(scope="function")
def first_new_book(books_collector):
    return books_collector.add_new_book(data.BOOK_1[0])


@pytest.fixture(scope="function")
def second_new_book(books_collector):
    return books_collector.add_new_book(data.BOOK_2[0])


@pytest.fixture(scope="function")
def first_book_with_genre(books_collector):
    return books_collector.set_book_genre(data.BOOK_1[0], data.BOOK_1[1])


@pytest.fixture(scope="function")
def favorite_book(books_collector):
    return books_collector.add_book_in_favorites(data.BOOK_1[0])


@pytest.fixture(scope="function")
def books_collection(books_collector):
    for book, genre in data.BOOKS:
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
