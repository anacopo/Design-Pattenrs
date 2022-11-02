
from Element import Element


class TableOfContents(Element):
    def __init__(self, something):
        self.something = something

    def print(self):
        print(f"Table of contents: {self.something}")