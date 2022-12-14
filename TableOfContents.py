
from Element import Element
from Visitor import Visitor


class TableOfContents(Element):
    def __init__(self, something):
        self.something = something

    def print(self):
        print(f"Table of contents: {self.something}")

    def accept(self, visitor: Visitor):
        visitor.visitTableOfContents(self)
