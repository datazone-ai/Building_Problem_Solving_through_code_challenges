# Day 6 challenge
# get user name from email

def user_name() -> str:
    email = input("Email: ")

    # if email is abiola@gmail.com we a tuple (abiola, @, gmail.com)
    user_name, separator, domain =  email.partition('@') # unpack tuple
    return user_name

print(f"user_name is {user_name()}")
