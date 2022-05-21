#  import module using import module

from auth_module import file, is_user_authenticated # import 
# import auth_module   # import whole module [file]

is_authenticated = is_user_authenticated('username', 'password')
print("Is User Authenticated ? " + str(is_authenticated))

is_authenticated = is_user_authenticated('randomun', 'randompw')
print("Is User Authenticated ? " + str(is_authenticated))