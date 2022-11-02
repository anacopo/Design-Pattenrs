class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    
    def print(self):
        print(f"Author: {self.name, self.surname}")