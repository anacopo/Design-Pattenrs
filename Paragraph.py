from Element import Element
from AlignStrategy import AlignStrategy
from Visitor import Visitor

class Paragraph(Element):
    def __init__(self, text: str):
        self.text = text 
        self.textAlignment = None
    
    def print(self):
        if self.textAlignment is None:
            print(f"Paragraph: {self.text}")
        else:
            self.textAlignment.render(self)

    def setAlignment(self, a: AlignStrategy):
        self.textAlignment = a

    def accept(self, visitor: Visitor):
        visitor.visitParagraph(self)
