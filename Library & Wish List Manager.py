# Owned books
book_name1 = input("Enter a name of a book you own:\n")
book_name2 = input("Enter a name of another book you own (or press enter to skip):\n")

library = []
if book_name1:
    library.append(book_name1)
if book_name2:
    library.append(book_name2)

print(f"\nYour library is: {library}\n")

# Wish list
wish_book1 = input("Enter a name of a book you wish to have in the future:\n")
wish_book2 = input("Enter a name of another book you wish to have in the future (or press enter to skip):\n")

wish_list = []
if wish_book1:
    wish_list.append(wish_book1)j5
if wish_book2:
    wish_list.append(wish_book2)

print(f"\nYour wish list is: {wish_list}\n")

# Acquired book
book_acquired = input("Enter a name of a book from your wish list you have acquired (or press enter to skip):\n")

if book_acquired in wish_list:
    wish_list.remove(book_acquired)
    library.append(book_acquired)

# Donate book
donate_book = input("Enter a book you want to donate from your library (or press enter to skip):\n")

if donate_book in library:
    library.remove(donate_book)

# Final result
print("\nFinal Library:", library)
print("Final Wish List:", wish_list)
