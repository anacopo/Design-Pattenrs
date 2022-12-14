from Element import Element
from Visitor import Visitor

class Table(Element):
    def __init__(self, title):
        self.title = title

    def print(self):
        print(f"Table with Title: {self.title}")

    def accept(self, visitor: Visitor):
        visitor.visitTable(self)
