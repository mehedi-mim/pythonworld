import time
# Define a class
class Fruit:
    pass

# Assign the class object into a variable
c = Fruit
print(c)

# Add attributes to the class
Fruit.age = 0
print(Fruit.age)

# Pass the class object as an argument
def display(class_obj):
    print(class_obj)

display(Fruit)

# Copy the class object
import copy

Fruit2 = copy.deepcopy(Fruit)
print(Fruit2)