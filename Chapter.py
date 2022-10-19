from SubChapter import SubChapter

class Chapter:
    def __init__(self, name):
        self.name = name
        self.subchapters = [] 

    def createSubChapter(self, subchapter_name):
        self.subchapters.append(SubChapter(subchapter_name))
        return len(self.subchapters)

    def getSubChapter(self, index):
        return self.subchapters[index-1]

    def print(self):
        print("Chapter: {self.name}")
        for sc in self.subchapters:
            sc.print()