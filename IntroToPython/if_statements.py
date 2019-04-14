print("IF statements")

'''
known_people = ["John", "Anna", "Mary"]
person = input("Please enter person name: ")

if person.capitalize() in known_people:
    print(person + " is known person")
else:
    print(person + " is unknown person")

'''


def who_do_you_know():
    # Ask the user for a list of people they know
    # Split the string into a list
    user_input = input("Please enter names of people (separated by space) you know and press ENTER: ")
    names = list(name.strip().capitalize() for name in user_input.split(" "))
    #print(names)
    return names


def ask_user(names):
    # Ask user for their name
    # See if their name is in the list of people they know
    # Print out that they know the person
    user_name = input("Please enter your name and press ENTER: ")
    if user_name.capitalize() in names:
        print("You know the person")
    else:
        print("You do not know the person")


ask_user(who_do_you_know())

