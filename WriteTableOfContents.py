from Visitor import Visitor
from Book import Book
from Section import Section
from TableOfContents import TableOfContents
from Paragraph import Paragraph
from ImageProxy import ImageProxy
from Image import Image
from Table import Table

class WriteTableOfContents(Visitor):

    def __init__(self) -> None:
        self.toc = ''
        self.page = 1

    def visitParagraph(self, paragraph):
        self.page += 1

    def visitSection(self, section):
        self.toc += f"{section.title} ... {self.page}"

    def visitImage(self, image):
        self.page += 1
    
    def visitImageProxy(self, imageProxy):
         self.page += 1

    def visitTable(self, table):
        self.page += 1

    def getToc(self):
        return self.toc

    def visitBook(self, book):
        pass 

    def visitTableOfContents(self, tableOfContents):
        pass
        

