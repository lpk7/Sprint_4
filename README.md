# qa_python
### Написаны тесты:
1. def test_add_new_book_two_books_success - проверка добавления в books_genre 2 валидных книг с использованием функции `get_books_genre` 
2. def test_set_book_genre_books_success - проверка присвоения книге жанра, с использованием функций `set_book_genre` и `get_book_genre`
3. def test_get_books_with_specific_genre_find_books_by_genre - проверка получения списка книг по жанру
4. def test_get_books_for_children_list_exclude_horror_and_detective - проверка создания списка детских книг
5. def test_add_book_in_favorites_success - проверка добавление книги в избранное
6. def test_delete_book_from_favorites_success - проверка добавления и последующего удаления книги из избранного
7. def test_get_list_of_favorites_books - проверка получения списка избранных книг
8. def test_add_new_book_again_negative - проверка повторного добавления книги
9. def test_add_new_book_with_invalid_name_negative - проверка добавления книг с невалидным именем

#### В файл **conftest.py** добавлены фикстуры:
books_collector
first_new_book
second_new_book
first_book_with_genre
favorite_book
books_collection

#### Коллекции вынесены в файл **data.py**
