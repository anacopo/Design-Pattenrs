from Image import Image
from Paragraph import Paragraph
from Table import Table

class SubChapter:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def createNewParagraph(self, paragraph_text):
        self.elements.append(Paragraph(paragraph_text))

    def createNewImage(self, image_name):
        self.elements.append(Image(image_name))

    def createNewTable(self, table_title):
        self.elements.append(Table(table_title))

    def print(self):
        print(f"Subchapter: {self.name}")
        for el in self.elements:
            el.print()
    