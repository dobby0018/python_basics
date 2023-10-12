class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Creating an instance of the Person class
john = Person("John", 30)

# The __init__ method sets the attributes 'name' and 'age' for the 'john' object
print(john.name)  # Accessing the 'name' attribute of the 'john' object
print(john.age)   # Accessing the 'age' attribute of the 'john' object

# Calling the 'introduce' method to get a formatted introduction
print(john.introduce())
