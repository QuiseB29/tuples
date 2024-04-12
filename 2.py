def add_book(library,book,author):
    library.append((book,author))
    return library


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

library = add_book(library, "The Great Gatsby", "F. Scott fitzgerald")

print(library)