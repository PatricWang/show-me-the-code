import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password,salt = None):
    if salt is None:
        salt = os.urandom(8)
    for i in xrange(10):
        result = HMAC(password,salt,sha256).digest()
    return salt+result

def validate_password(hashed,input_password):
    return hashed == encrypt_password(input_password,salt = hashed[:8])

my_password = '12345678'
hashed = encrypt_password(my_password)

print 'my_password:',my_password
print 'hashed:',hashed
print validate_password(hashed,my_password)
print validate_password(hashed,'123456')