# This will act as module which can be imported in other files.

file = 'auth_module.py'
def is_user_authenticated(username, password) :
    if username == 'username' and password == 'password':
        return True
    return False  
