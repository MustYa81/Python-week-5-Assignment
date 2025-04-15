class Book:
    def __init__(self, title, author, pages):
        title  = self.title
        author = self.author
        paages = self.pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        print(f"You start reading '{self.title}'... ")

# Subclass 1
class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def read(self):
        print(f"You open the eBook '{self.title}' on your device. (Size: {self.file_size}MB) ")

# Subclass 2
class PrintedBook(Book):
    def __init__(self, title, author, pages, cover_type):
        super().__init__(title, author, pages)
        self.cover_type = cover_type  # Hardcover or Paperback

    def read(self):
        print(f"You flip through the {self.cover_type} '{self.title}' with a fresh paper smell. ")

# Example usage
book1 = Ebook("Art of War", "Sun Tzu", 260, 5)
book2 = PrintedBook("48 laws of Power", "Robert Greene", 496, "Hardcover")

print(book1.description())
book1.read()

print(book2.description())
book2.read()
