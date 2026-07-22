from abc import ABC, abstractmethod
class ABSclass(ABC):
    def print(self,x):
        print("past value :", x)
    @abstractmethod
    def task(self):
        print("we are inside ABSclass task")
class test_class(ABSclass):
    def task(self):
        print("we are inside task_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)