from abc import ABC, abstractmethod


class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
