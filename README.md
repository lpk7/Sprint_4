# qa_python
### Написаны тесты:
1. test_add_new_book_two_books_success - проверка добавления в books_genre 2 валидных книг
2. test_set_book_genre_books_success - проверка присвоения книге жанра, с использованием функций
3. test_get_books_with_specific_genre_find_books_by_genre - проверка получения списка книг по жанру
4. test_get_books_for_children_list_exclude_horror_and_detective - проверка создания списка детских книг
5. test_get_books_genre_success - проверка получения коллекции books_genre
6. test_get_book_genre_by_name_success - проверка получения жанра книги по имени
7. test_add_book_in_favorites_success - проверка добавление книги в избранное
8. test_delete_book_from_favorites_success - проверка добавления и последующего удаления книги из избранного
9. test_get_list_of_favorites_books - проверка получения списка избранных книг
10. test_add_new_book_again_negative - проверка повторного добавления книги
11. test_add_new_book_with_invalid_name_negative - параметризованная проверка добавления книг с невалидной длинной имени
12. test_add_new_book_with_valid_name_length_success - параметризованная проверка добавления книг с корректной длинной имени (от 1 до 40)

#### В файл **conftest.py** добавлены фикстуры:
books_collector
first_new_book
first_book_with_genre
favorite_book
books_collection

#### Коллекции вынесены в файл **data.py**
