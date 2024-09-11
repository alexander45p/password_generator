import string
import random

longitude = int(input("enter password size: "))

characters = string.ascii_letters + string.punctuation

password = "".join(random.choice(characters) for i in range(longitude))

print("the generated password is")


