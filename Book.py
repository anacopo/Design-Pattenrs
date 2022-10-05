class Book:
    def __init__(self, name):
        self.name = name
        self.paragaph = []
        self.image = []
        self.table = []

    def createNewParagraph(self, paragraph_name):
        self.paragaph.append(paragraph_name)

    def createNewImage(self, image_name):
        self.image.append(image_name)
    
    def createNewTable(self, table_name):
        self.table.append(table_name)

    def print(self):
        print("Book name: " + self.name)
        if(len(self.paragaph) != 0):
            print("Book paragraphes: %s" % self.paragaph)
        if(len(self.image) != 0):
            print("Book Images: %s" % self.image)
        if(len(self.table) != 0):
            print("Book Tables: %s" % self.table)


