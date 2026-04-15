import pytest
import data
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_two_books_success(
        self, books_collector
    ):
        books_collector.add_new_book(data.BOOK_1[0])
        books_collector.add_new_book(data.BOOK_2[0])
        assert len(books_collector.get_books_genre()) == 2

    def test_set_book_genre_books_success(
        self, books_collector
    ):
        books_collector.add_new_book(data.BOOK_1[0])
        books_collector.set_book_genre(data.BOOK_1[0], data.BOOK_1[1])
        assert books_collector.get_book_genre(data.BOOK_1[0]) == data.BOOK_1[1]

    def test_get_books_with_specific_genre_find_books_by_genre(
        self, books_collector, books_collection
    ):
        assert len(books_collector.get_books_with_specific_genre("Детективы")) == 2

    def test_get_books_genre_success(self, books_collector, books_collection):
        assert len(books_collector.get_books_genre()) == 6

    def test_get_book_genre_by_name_success(self, books_collector, first_book_with_genre):
        assert books_collector.get_book_genre(data.BOOK_1[0]) == data.BOOK_1[1]

    def test_get_books_for_children_list_exclude_horror_and_detective(
        self, books_collector, books_collection
    ):
        books_for_children = books_collector.get_books_for_children()
        for book in books_for_children:
            assert (
                books_collector.get_book_genre(book)
                not in books_collector.genre_age_rating
            )

    def test_add_book_in_favorites_success(
        self, books_collector, first_book_with_genre
    ):
        books_collector.add_book_in_favorites(data.BOOK_1[0])
        assert data.BOOK_1[0] in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success(
        self, books_collector, first_book_with_genre, favorite_book
    ):
        books_collector.delete_book_from_favorites(data.BOOK_1[0])
        assert data.BOOK_1[0] not in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(
        self, books_collector,first_book_with_genre, favorite_book
    ):
        favorites = books_collector.get_list_of_favorites_books()
        assert len(favorites) > 0

    def test_add_new_book_again_negative(self, books_collector):
        books_collector.add_new_book(data.BOOK_1[0])
        books_collector.add_new_book(data.BOOK_1[0])
        assert len(books_collector.books_genre) == 1

    @pytest.mark.parametrize("book_names", [("Прогнозирование цен на акции — подход к прогнозированию цены акций с использованием..."),
        ("")])
    def test_add_new_book_with_invalid_name_negative(self, books_collector, book_names):
        books_collector.add_new_book(book_names)
        assert len(books_collector.books_genre) == 0

    @pytest.mark.parametrize("book_names", [("1984"), ("F"), ("Книга с названием из сорока символов 123")])
    def test_add_new_book_with_valid_name_length_success(self, books_collector, book_names):
        books_collector.add_new_book(book_names)
        assert len(books_collector.books_genre) == 1
