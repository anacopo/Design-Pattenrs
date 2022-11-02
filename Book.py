from Author import Author
from Section import Section

class Book(Section):
    def __init__(self, title: str):
        super().__init__(title)
        self.authors = []

    def addAuthor(self, author: Author):
        self.authors.append(author)

    def addContent(self, content):
        super().add(content)

    def print(self):
        print(f"Book: {self.title}")
        for author in self.authors:
            author.print()
        for el in self.children:
            el.print()
