"""Program to check if a password length"""



def main():
    min_length= 10
    password = get_password()


    while len(password) != min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = get_password()

    print_astricks(password)


def print_astricks(password: str):
    print('*' * len(password))


def get_password() -> str:
    password = input("Please Enter password: ")
    return password

main()