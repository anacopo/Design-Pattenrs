from Book import Book
from Author import Author

if __name__ == '__main__':
    discoTitanic = Book("Disco Titanic")
    rpGheo = Author("Radu Pavel Gheo")

    discoTitanic.addAuthor(rpGheo)
    indexChapterOne = discoTitanic.createChapter("Capitolul 1")
    chp1 = discoTitanic.getChapter(indexChapterOne)
    indexSubChapterOne = chp1.createSubChapter("Subcapitolul 1.1")
    scOneOne = chp1.getSubChapter(indexSubChapterOne)

    scOneOne.createNewParagraph("Paragraph 1")
    scOneOne.createNewParagraph("Paragraph 2")
    scOneOne.createNewParagraph("Paragraph 3")
    scOneOne.createNewImage("Image 1")
    scOneOne.createNewParagraph("Paragraph 4")
    scOneOne.createNewTable("Table 1")
    scOneOne.createNewParagraph("Paragraph 5")

    scOneOne.print()