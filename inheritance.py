class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self,sound):
        print(f"{self.name} speaks {sound}")
    def eat(self):
        print("it will eat")
class Dog(Animal):
    def __init__(self,breed,name):
        super().__init__(name)
        self.breed=breed
Dog1=Dog("Labrador","Buddy")
Dog1.speak("Woof")
Dog1.eat()  