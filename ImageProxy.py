from Element import Element
from Image import Image

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