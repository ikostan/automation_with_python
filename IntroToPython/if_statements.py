print("IF statements")

known_people = ["John", "Anna", "Mary"]
person = input("Please enter person name: ")

if person.capitalize() in known_people:
    print(person + " is known person")
else:
    print(person + " is unknown person")

