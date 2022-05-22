# import that class
from SecUser import SecUser

sec_user = SecUser('badripaudel', 'password')

if(sec_user.is_username_valid(sec_user.username)):
    print('username is valid')

else:
     print('username is invalid')


# print(sec_user.get_username())
print('password is : ', sec_user.get_password()) 
# print('password is : ', sec_user.__password) # gives error as __password has private access

# directly access the attribute. by default in python, we can access attributes outside of the class too if it's public
# we can hide using the concept of data hiding. In order to make data attribute private, variable has to be preceded with __ [double underscores]

print(sec_user.match_credentials('badripaudel77', 'password'))
print('-----------')
print('is user valid: ', sec_user.match_credentials('badripaudel', 'password'))