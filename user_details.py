# Print the name of user after taking input from the user
def user_details():
    first_name = input("What is your first name?")
    mid_name = input("What is your middle name?")
    last_name = input("What is your last name?")
    print(f"Welcome Aboard,{first_name} {mid_name} {last_name}!")

    age = int(input("What is your age? Please enter digits only"))
    print(f"Hi {first_name}, your age is {age}.")

    address= input("Please enter your address?")
    print(f"Thanks for sharing your address. Your address is: {address}")

    postcode = input("Please enter a valid postcode")
    if(len(postcode))==6:
        print("Postcode is valid. Thanks for sharing")
    else:
        print("Invalid postcode")

    house_number = input("Please enter your house number")
    if house_number.isdigit():
        print("Thanks for sharing a valid house number")
    else:
        print("Invalid house number")

    salary = float(input("What is your salary? Please enter digits only"))
    print(f"Hi {first_name}, your salary is {salary}.")

    hobbies = input("What are your hobbies?")
    print(f"Hi {first_name}, thanks for sharing your hobbies, they are {hobbies}.")

user_details()

