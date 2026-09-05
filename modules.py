# A module is basically a file containing a set of functions to include 
# in your application. There are core python modules, module you
# can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
from datetime import date
import time
from time import time

# pip modules
import camelCase

# custom modules
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

camel = camelCase.CamelCase()
text = 'hello there world'
print(camel.hump(text))

email = 'test@test.com'
if validator.validate_email(email):
    print('Email is valid')
else:
    print('Not an email')