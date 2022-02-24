#### https://www.codingem.com/metaclasses-in-python/
Now you understand what is a metaclass in Python. More importantly, you now know how to alter the way classes are constructed in Python.

Writing custom metaclasses can be useful because this way you can enforce constraints on how classes are created.

For instance, you can write a metaclass that does not allow some attributes to be used at all. Or you could write a metaclass that disables inheritance.

You can affect anything about creating a class with a metaclass.

Writing a metaclass is useful when you are writing module/library code and you want the classes to follow a specific structure.

When a developer then uses this library, for example, to inherit from a specific class, you can ensure the class has a specific function to make it work.