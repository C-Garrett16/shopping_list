import pickle
import readline

readline.parse_and_bind("history-search-backward: up")
readline.parse_and_bind("history-search-forward: down") 

shopping_list = []
item = ""


# Open the list from a file
with open("shopping_list.data", "rb") as f:
    shopping_list = pickle.load(f)




def help():
    print("Welcome to the shopping list program! Here are some commands you can use:")
    print("""
            You can add items to the list by typing "add" then following the prompts.".
            You can remove items from the list by typing "remove" then following the prompts.
            You can clear the list by typing "clear".
            You can display the list by typing "list".
            You can quit the program by typing "quit".
            """)


def display_list():
    print("You have " + str(len(shopping_list)) + " items on your list")
    print("----------------------------------------------------------------")
    for item in shopping_list:
        print(item)


def add_to_list():
    item = input("What would you like to add? ")
    if item in shopping_list:
        print(item + " is already on the list")
        return
    else:
        shopping_list.append(item)
        print(item + " has been added to the list")
        display_list()


def remove_from_list():
    display_list()
    item = input("What would you like to remove? ")
    if item in shopping_list:
        print(item + " has been removed from the list")
        shopping_list.remove(item)
        display_list()
    # elif user_input.startswith("remove"): ## WIP
    ##    if len(user_input.split()) > 1:
    ##       remove_from_list(user_input.split()[1])
    else:
        print(item + " is not on the list")
        display_list()


def clear_list():
    if len(shopping_list) > 0:
        user_input = input("Are you sure you want to clear the list? (y/n) ")
        if user_input == "y":
            print("The list has been cleared")
            shopping_list.clear()
            display_list()
    else: print("The list is already empty")

def write_to_file():
    with open("shopping_list.data", "wb") as f:
        pickle.dump(shopping_list, f)
        print("The list has been saved to shopping_list.data")


help()

user_input = ""

command_dict = {
    "list": display_list,
    "remove": remove_from_list,
    "clear": clear_list,
    "add": add_to_list,
    "write" : write_to_file,
    "help": help,
    "quit": quit
}



while user_input != "quit":

    user_input = input("> ")

    if user_input in command_dict.keys():
        command_dict[user_input]()

    else:
        print("Invalid command")

print(shopping_list)
