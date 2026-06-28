
import random
import string

print("=" * 50)
print("        PASSWORD GENERATOR")
print("=" * 50)

while True:

    try:
        length = int(input("\nEnter the password length (Minimum 6): "))

        if length < 6:
            print("Password length should be at least 6.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    print("\nChoose Password Complexity")
    print("1. Letters Only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Characters")

    choice = input("Enter your choice (1/2/3): ")

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if choice == "1":
        characters = letters

    elif choice == "2":
        characters = letters + numbers

    elif choice == "3":
        characters = letters + numbers + symbols

    else:
        print("Invalid Choice! Try Again.")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n" + "=" * 50)
    print("Generated Password:")
    print(password)
    print("=" * 50)

    again = input("\nDo you want to generate another password? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using Password Generator!")
        break