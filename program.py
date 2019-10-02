import string
import random


chars = string.ascii_letters + string.digits + string.punctuation


def main():
    """The main program"""
    # get length of the password the user wants
    length = input("How many characters do you want in the password? ")
    print(f"You have selected a {length}-character length password.")

    password = password_generation(length)
    result(password)


def result(password):
    """Produces the password"""
    print()
    print("Here you go:")
    print(password)


def password_generation(length):
    """Generate the password"""
    password = "".join(random.sample(chars, int(length)))
    return password


if __name__ == "__main__":
    main()
