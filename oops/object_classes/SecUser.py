# classes can be created using class keyword followed by class name [camel casing in case of class name]
# Parent class name is the name of the class this want to inherit, if nothing is specified, object is used , just like java extends Object class by default.
# __init__() is created by default which does nothing if no other constructors are created, just like in java
# syntax : class ClassName(Parent Class Name): 
#                    class body ....
# To create object , in python we can just call ClassName() or ClassName(arguments) if we have passed arguments in constructor.
# Just like in Kotlin, python doesn't have new keyword

class SecUser(object):
    def __init__(self, username, password):
        # self is equivalent to this keyword in java, __init__() equivalent to constructor function.
        self.username = username
        # self.password = password # by default public access 
        self.__password = password # __ make variable private i.e can't access outside of this class.
        print('log [Constructor] : username = ', self.username, 'password = ', self.__password)

    def is_username_valid(self, username):
        if(username.isalpha()):
            return True
        else :
            return False

    def get_password(self):
        return self.__password

    def match_credentials(self, username, password):
        print('log [match_credentials self]: username = ', self.username, ' password = ', self.__password)

        if(self.username == username and self.__password == password):
            return True
        return False        

