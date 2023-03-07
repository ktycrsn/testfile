def main():
    encode_running = True
    menu = 'Menu \n------------- \n1. Encode  \n2. Decode  \n3. Quit'
    print(menu)
    while encode_running:
        choice = input("\nPlease enter an option: ")
        if choice == "1":
            encoding = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            new = encode(encoding)
            print(menu)
        elif choice == "2":
            normal = decoder(encode(encoding))
            print(f'The encoded password is {new}, and the original password is {normal}.\n')
            print(menu)
        elif choice == "3":
            encode_running = False



def encode(encoding):
    encoded = ""
    for num in encoding:
        new_digit = str(((int(num) + 3) % 10))
        encoded += new_digit
    return encoded

# decodes encoded password
def decoder(password): #added a comment since I don't have a partner

    decoded = ""

    # iterates over the string
    for i in range(len(password)):
        subtract = int(password[i]) - 3

        if subtract < 0:
            subtract += 10
        decoded += str(subtract)

    return decoded


if __name__ == "__main__":
    main()