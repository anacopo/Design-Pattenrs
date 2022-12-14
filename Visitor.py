from abc import ABC, abstractmethod
# from Book import Book
# from Section import Section
# from TableOfContents import TableOfContents
# from Paragraph import Paragraph
# from ImageProxy import ImageProxy
# from Image import Image
# from Table import Table

class Visitor(ABC):
    
    @abstractmethod
    def visitBook(book):
        pass
        
    @abstractmethod
    def visitSection(section):
        pass

    @abstractmethod
    def visitTableOfContents(tableOfContents):
        pass

    @abstractmethod
    def visitParagraph(paragraph):
        pass

    @abstractmethod
    def visitImageProxy(imageProxy):
        pass

    @abstractmethod
    def visitImage(image):
        pass

    @abstractmethod
    def visitTable(table):
        pass