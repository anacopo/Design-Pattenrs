from Author import Author
from Chapter import Chapter

class Book:
    def __init__(self, name):
        self.name = name
        self.chapters = []

    def addAuthor(self, author_name):
        self.author = Author(author_name)

    def createChapter(self, chapter_name):
        self.chapters.append(Chapter(chapter_name))
        return len(self.chapters)

    def getChapter(self, index):
        return self.chapters[index-1]

    def print(self):
        print(f"Book: {self.name}")
        for ch in self.chapters:
            ch.print()