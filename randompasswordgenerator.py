import random
import string
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation
all=lower+upper+num+symbols
temp=random.sample(all,12)
password=''.join(temp)
print('your generated password is:',password)