"""

What is duck typing?
**********************
Duck typing is one of the most useful concepts in object-oriented programming in Python. 
Using duck typing, we can implement polymorphism without using inheritance.
We say that if an object quacks like a duck, swims like a duck, eats like a duck or in short, 
acts like a duck, that object is a duck.
****************************************************
Let us see an example to implement the duck typing
****************************************************
Explanation
************
In line 46, the type of animal is not defined in the definition of the method Sound.
Type of animal is determined when the method is called, so it does not matter which 
object type you are passing as a parameter in the Sound() method, 
what matters is that the Speak() method should be defined in all the classes whose 
objects are passed in the Sound() method.
We can use any property or method of animal in the AnimalSound class 
as long as it is declared in that class.
************
Conclusion
************
Now coming back to why it is called Duck typing: So, if a bird speaks like a duck, 
swims like a duck, and eats like a duck, that bird is a duck.
Similarly, in the below example, the animal object does not matter in the definition 
of the Sound method as long as it has the associated behavior, Speak(), defined in 
the object’s class definition. In layman terms, since both the animals, dog and cats, 
can speak like animals, they both are animals. This is how we have achieved polymorphism 
without inheritance
"""


class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)
