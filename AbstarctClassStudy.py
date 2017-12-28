#Example of abstarct Class


from abc import ABC, abstractmethod


class AbstractAnimal(ABC):

#abstract method to also to be instantiaded in the actual class
    @abstractmethod
    def MakeNoise(self):
        print("I am abstacrt like Picasso i cant make sound")


class ActualDog(AbstractAnimal):
    def MakeNoise(self):
#super will run the function from the super class
        super().MakeNoise()
        print("well i am a dog so woof!!")

d=ActualDog()

d.MakeNoise()