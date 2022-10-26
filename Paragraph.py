from Element import Element

class Paragraph(Element):
    def __init__(self, text):
        self.text = text 
    
    def print(self):
        print(f"Paragraph: {self.text}")