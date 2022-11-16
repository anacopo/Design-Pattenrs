from Book import Book
from Author import Author
from Section import Section
from Paragraph import Paragraph
from Image import Image
from ImageProxy import ImageProxy
from AlignCenter import AlignCenter
from AlignLeft import AlignLeft
from AlignRight import AlignRight

import time

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
    print("Printing without Alignment")
    print()
    cap1.print()

    p1.setAlignment(AlignCenter())
    p2.setAlignment(AlignRight())
    p3.setAlignment(AlignLeft())

    print()
    print("Printing with alignment")
    print()
    cap1.print()
    # startTime = time.time()
    # img1 = ImageProxy("Pamela Anderson")
    # img2 = ImageProxy("Kim K")
    # img3 = ImageProxy("Kirby Griffin")
    # playboyS1 = Section("Front Cover")
    # playboyS1.add(img1)
    # playboyS2 = Section("Summer Girls")
    # playboyS2.add(img2)
    # playboyS2.add(img3)
    # playboy = Book("Playboy")
    # playboy.addContent(playboyS1)
    # playboy.addContent(playboyS2)
    # endTime = time.time()

    # print(f"Creation of the content took {endTime-startTime} milliseconds")

    # startTime = time.time()
    # playboyS1.print()
    # endTime = time.time()

    # print(f"Printing of the section 1 took {endTime-startTime} milliseconds")

    # startTime = time.time()
    # playboyS1.print()
    # endTime = time.time()

    # print(f"Printing again section 1 took {endTime-startTime} milliseconds")