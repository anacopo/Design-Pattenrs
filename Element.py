from abc import ABC, abstractmethod
from Visitor import Visitor

class Element(ABC):
    
    @abstractmethod
    def print():
        pass

    @abstractmethod
    def accept(visitor):
        pass
