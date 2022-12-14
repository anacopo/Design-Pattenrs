#from Book import Book
from Author import Author
from Section import Section
from Paragraph import Paragraph
from Image import Image
from ImageProxy import ImageProxy
from AlignCenter import AlignCenter
from AlignLeft import AlignLeft
from AlignRight import AlignRight
from Table import Table
from BookStatistics import BookStatistics
from TableOfContents import TableOfContents
from WriteTableOfContents import WriteTableOfContents

if __name__ == '__main__':
    cap1 = Section("Capitolul 1")
    p1 = Paragraph("Paragraph 1")
    cap1.add(p1)
    p2 = Paragraph("Paragraph 2")
    cap1.add(p2)
    p3 = Paragraph("Paragraph 3")
    cap1.add(p3)
    p4 = Paragraph("Paragraph 4")
    cap1.add(p4)
    cap1.add(ImageProxy("ImageOne"))
    cap1.add(Image("ImageTwo"))
    cap1.add(Paragraph("Some text"))
    cap1.add(Table("Table 1"))
    
    cap2 = Section("Capitolul 2")

    stats = BookStatistics()
    cap1.accept(stats)
    stats.printStatistics()

    toc = WriteTableOfContents()
    cap1.accept(toc)
    tableOfContents = TableOfContents(toc.getToc())
    tableOfContents.print()
