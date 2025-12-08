disk_size_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

book_chars = pages * lines_per_page * chars_per_line
book_size_bytes = book_chars * bytes_per_char

disk_size_bytes = disk_size_mb * 1024 * 1024

books_count = int(disk_size_bytes // book_size_bytes) # TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_count)
