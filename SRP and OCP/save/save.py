from abc import ABC, abstractmethod


class SavetoDB(ABC):
    @abstractmethod
    def saveToDB(self, shopping_cart):
        pass