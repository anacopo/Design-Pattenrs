from Element import Element

class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name

    def print(self):
        print(f"Image with name: {self.image_name}")