# TODO Найдите количество книг, которое можно разместить на дискете
DISK_SIZE = 1.44 * 1024 * 1024  # размер диска в байтах
SHEETS_PER_BOOK = 100
LINES_PER_PAGE = 50
LETTERS_PER_LINE = 25
SYMBOL_SIZE = 4

one_book_size = SYMBOL_SIZE * LETTERS_PER_LINE * LINES_PER_PAGE * SHEETS_PER_BOOK
amount_of_books_per_disk = DISK_SIZE // one_book_size

print("Количество книг, помещающихся на дискету:", int(amount_of_books_per_disk))
