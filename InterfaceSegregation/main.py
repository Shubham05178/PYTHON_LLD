from abc   import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Eat(Employee):
    @abstractmethod
    def eat(self):
        pass
class Developer(Eat):
    def work(self):
        print("Developer is working")
    def eat(self):
        print("Developer is eating")
class Robot(Employee):
    def work(self):
        print("Robot is working")
d1=Developer()
d1.work()
d1.eat()
r1=Robot()
r1.work()