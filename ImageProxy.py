from Element import Element
from Image import Image
from Visitor import Visitor

class ImageProxy(Element):
    def __init__(self, url: str):
        self.url = url
        self.realImage = None
    
    def loadImage(self) ->Image:
        if self.realImage is None:
            self.realImage = Image(self.url)
        return self.realImage

    def print(self):
        self.loadImage()
        self.realImage.print()

    def accept(self, visitor: Visitor):
        visitor.visitImageProxy(self)
        