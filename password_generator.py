import random
import string


def password_generator():
    length = int(input("enter length for you password: "))
    if length == 0:
        quit()
    else:
        str = string.ascii_letters+string.punctuation+string.hexdigits+string.digits
        pas = random.sample(str,length)
        password = "".join(pas)
        print("your password is: ",password)



print("create your password")
while True:
    password_generator()


