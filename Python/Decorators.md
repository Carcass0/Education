## @Property
After applying the property decorator, you are allowed to define a getter, setter, and deleter for the attribute. The function with the property decorator acts as the getter. Setters and deleters allow for modifying the behaviour of according commands.
```python
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value
    
    @name.deleter 
    def name(self):
        print('Deleting..')
        del self.__name

std = Student('Steve')
print(std.name)
del std.name
print(std.name) 
```

## @classmethod
Used to declare a method in the class as a class method that can be called using `ClassName.MethodName()`. The class method can also be called using an object of the class.

 @classmethod Characteristics
- Declares a class method.
- The first parameter must be `cls`, which can be used to access class attributes.
- The class method can only access the class attributes but not the instance attributes.
- The class method can be called using `ClassName.MethodName()` and also using object.
- It can return an object of the class.

The class method can also be used as a factory method to get an object of the class

## @staticmethod
A built-in decorator that defines a static method in the class in Python. A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.

 @staticmethod Characteristics
- Declares a static method in the class.
- It cannot have `cls` or `self` parameter.
- The static method cannot access the class attributes or the instance attributes.
- The static method can be called using `ClassName.MethodName()` and also using `object.MethodName()`.
- It can return an object of the class.

