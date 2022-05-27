# Inheritance in general is a feature of most of the programming languages which allows us to reuse and modify the attributes and 
# behaviors from the other classes.
# Usaully have the concept of parent and child classes. 
# Parent class can be inherited by the child class
# In python syntax is different but principle is just like in Java [at least  basic concept is very much similar]
# Syntax : 
# ParentClass(ChildClass):
# ....

class ShapeArea:
    def __init__(self, type, color = 'RED'):
        self.color = color
        self.type = type
        print('[logging.debug] ' +  color + ' ' + type + '  shape ')


    def get_color(self) :
        return self.color

    

