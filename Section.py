from Element import Element


class Section(Element):
    def __init__(self, title: str):
        self.title = title
        self.children = []

    def add(self, el: Element):
        self.children.append(el)

    def remove(self, el: Element):
        self.children.remove(el)

    def get(self, id: int) -> Element:
        return self.children[id]
    
    def print(self):
        print(self.title)
        for child in self.children:
             child.print()