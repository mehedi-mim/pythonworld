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


def give():
    class Something:
        pass
    return Something

# Example call
s = give()
print(s)

Fruit = type('Fruit',(),{})
banana = Fruit()
print(banana)

Fruit = type('Fruit', (), {'color': 'Green'})
banana = Fruit()
print(banana.color)

def info(self):
    print(self.color)

Fruit = type('Fruit', (), {'color': 'Green', 'info': info})
apple = Fruit()
apple.info()


class Organic:
    pass

Fruit = type('Fruit', (Organic, ), {})


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        modified_attrs = {}
        for name,value in attrs.items():
            if name.startswith("__"):
                modified_attrs[name] = value
            else:
                modified_attrs[name.upper()] = value
        return type(class_name, bases,modified_attrs)

class Fruit(metaclass=Meta):
    def  myfunc(self):
        return "Hiiiiii"
    color = "Green"
    
    
f = Fruit()
print(f.COLOR)
print(f.MYFUNC())