import random
import string

def generate_password(length=16): # define the passwords length here
    chars = string.ascii_letters + string.digits + string.punctuation # define the set of characters to choose from

    # use a secure random source to generate the password
    rng = random.SystemRandom()

    # generate a password that includes at least one uppercase letter, one lowercase letter,
    # one digit, and one special character
    password = ""
    while True:
        password = ''.join(rng.choice(chars) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            break

    return password
    # returns you your own generated password
