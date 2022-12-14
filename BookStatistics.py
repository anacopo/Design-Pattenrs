from Visitor import Visitor
from Book import Book
from Section import Section
from TableOfContents import TableOfContents
from Paragraph import Paragraph
from ImageProxy import ImageProxy
from Image import Image
from Table import Table

class BookStatistics(Visitor):

    def __init__(self) -> None:
        self.images = 0
        self.tables = 0
        self.paragraphs = 0

    def visitImage(self, image: Image):
        self.images += 1

    def visitTable(self, table: Table):
        self.tables += 1

    def visitParagraph(self, paragraph: Paragraph):
        self.paragraphs += 1

    def printStatistics(self):
        print('Book statistics:')
        print(f"*** Number of images: {self.images}")   
        print(f"*** Number of tables: {self.tables}")
        print(f"*** Number of paragraphs: {self.paragraphs}")     

    def visitBook(self, book):
        pass

    def visitImageProxy(self, imageProxy):
        self.images += 1

    def visitSection(self, section):
        pass

    def visitTableOfContents(tableOfContents):
        pass  