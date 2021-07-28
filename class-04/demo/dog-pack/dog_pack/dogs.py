from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod

# class Dog(ABC):
#     # class property, accessible without an instance or from an instance
#     count = 0

#     """A simple dog class"""
#     def __init__(self, name="unknown"):
#         """Constructor"""
#         self.name = name
#         print("Dog created")
#         Dog.count += 1

#     # instance method
#     def sleep(self)-> str:
#         return "zzz"

#     @classmethod
#     def get_all_dog_count(cls):
#         return cls.count
    
#     @staticmethod
#     def get_characteristics():
#         return "Boxers are lovers, not fighters."
    
#     @abstractmethod
#     def bark():
#         pass



# hierarchy - relationships between things where one can be defined as containing the other; or as a special case of the other


class Dog(ABC): # Abstract classes are not intended to be instantiated

    # attribute or property
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        self.__class__.increase_count()

    def sleep(self):
        return "zzz"

    @abstractclassmethod
    def increase_count(cls):
        Dog.count += 1

    @abstractmethod   # definition or a signature of what should be implemented 
    def greet(self):
        return f"Default implementation"

    @abstractstaticmethod
    def get_characteristics():
        pass

    @classmethod
    def get_all_dog_count(cls):
        return cls.count

class Boxer(Dog):
    """
    A super cool dog
    """

    count = 0

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return super().increase_count()

    def greet(self): # the implementation of the abstract method
        return f"The name's {self.name}. Pleasure."

    @staticmethod
    def get_characteristics():
        return "Boxers are lovers, not fighters."

    @classmethod
    def get_breed_count(cls):
        return cls.count
class Puggle(Dog):
    """
    adorably spunky
    """

    count = 0

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return super().increase_count()

    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"

    @classmethod
    def get_breed_count(cls):
        return cls.count


if __name__ == "__main__":
    # dog = Dog("Fido") # create an instance of the Dog class
    dog = Boxer("Boxer")
    dog2 = Puggle("Puggle")
    dog3 = Puggle("Puggle of Awesomeness")
    
    print(Dog.get_all_dog_count()) # returns 3 because we created 3 Dogs
    print(Boxer.get_all_dog_count()) # returns 1 because the class Boxer gets passed as the first paremeter to the method
    print(Boxer.get_breed_count()) # returns 1 because the class Boxer gets passed as the first paremeter to the method
    print(Puggle.get_breed_count()) # returns 2 because the class Puggle gets passed as the first paremeter to the method
    # print(dog.name)
    # dog.name = "Buddy"
    # print(dog.name)
    # print(dog.sleep())
    # buster = Dog("Buster")

    # print(Dog.get_all_dog_count())
    # print(Dog.get_characteristics())
    # print(dog.get_characteristics())