""" Menu-driven score program"""
from prac_01.menus import choice
from prac_02.score import categorise_score


def main():
    print("Welcome to the Score Program.")
    score = get_vaild_score()

    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>>").upper()
        if choice == "P":
            result = categorise_score(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Thanks for using the program.")
        else:
            print("Invalid choice, please try again.")

def print_menu():
    """Display the menu options"""
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_vaild_score():
    """Prompt user until a valid score (0-100 inclusive) is entered"""
    score = int(input("Enter your score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score, must be between 0 and 100, please try again.")
    else:
        print("Please enter a valid number.")
    return score

def show_stars(score):
    """Print as many stars as the score."""
    print("*" * score)
main()