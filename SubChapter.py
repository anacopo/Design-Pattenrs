from Image import Image
from Paragraph import Paragraph
from Table import Table

class SubChapter:
    def __init__(self, name):
        self.name = name
        self.paragraphs = []
        self.images = []
        self.tables = []

    def createNewParagraph(self, paragraph_text):
        self.paragraphs.append(Paragraph(paragraph_text))

    def createNewImage(self, image_name):
        self.images.append(Image(image_name))

    def createNewTable(self, table_title):
        self.tables.append(Table(table_title))

    def print(self):
        print(f"Subchapter: {self.name}")
        for p in self.paragraphs:
            p.print()
        for i in self.images:
            i.print()
        for t in self.tables:
            t.print()