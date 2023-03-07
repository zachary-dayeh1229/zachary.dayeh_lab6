"""
Zachary Dayeh
Lab 6
Software Engineering
"""

def menu():  # menu display.

    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    menu_option = int(input("Please enter an option: "))

    return menu_option

def encode():  # encodes password.

    user_password = int(input("Please enter your password to encode: "))
    user_password = str(user_password)  # turns to string to iterate.
    user_password = [str((int(i) + 3)) for i in user_password]  # makes list with list comprehension from string.
    encoded_password = "".join(user_password)  # joins list.
    print("Your password has been encoded and stored!")
    print()

    return encoded_password  # returns the encoded password.

def decode(user_password):
    user_password = user_password
    decoded_password = [str((int(i)-3)) for i in str(user_password)]
    decoded_password = "".join(decoded_password)
    print(f"The encoded password is {user_password}, and the original password is {decoded_password}")
    print()

    return decoded_password


if __name__ == "__main__":

    display_menu = True  # boolean

    while display_menu == True:  # loops until user quits.

        menu_option = menu()  # calls menu to print and return value.

        if menu_option == 1:
            encoded_password = encode()  # calls encode function.

        if menu_option == 2:
            decoded_password = decode(encoded_password)

        if menu_option == 3:
            break