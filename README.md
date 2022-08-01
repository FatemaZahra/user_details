# User details

User details is a project in pycharm that takes input from the users, and displays it back to them.

## Overview of the code

```python
def user_details():
    first_name = input("What is your first name?")
    mid_name = input("What is your middle name?")
    last_name = input("What is your last name?")
    
 ```
 User details is a function that takes input from the user about their first name, middle name and last name.
 
 ```python
 print(f"Welcome Aboard,{first_name} {mid_name} {last_name}!")
 ```
 It then prints back the first, middle and last name after **concatinating** them.
 This method of concatination id called *formatted string literal* or *f-string*
 
There are other methods of concatination like using a `+` symbol.
```python
print(first_name + " " + mid_name+ " " + last_name+ " " +str(age))
```

**Casting:** It is a process in which we convert a literal of one type to another
```python
age = int(input("What is your age? Please enter digits only"))
    print(f"Hi {first_name}, your age is {age}.")
```

In this block of code age is converted into an integer after the user enters it as a string.

User address is also provided by the user

```python
address= input("Please enter your address?")
    print(f"Thanks for sharing your address. Your address is: {address}")
    
 ```

**len** is another method on python that gives back the length of the string. This block of code utilises the length method to check for a valid postcode

```python
postcode = input("Please enter a valid postcode")
    if(len(postcode))==6:
        print("Postcode is valid. Thanks for sharing")
    else:
        print("Invalid postcode")
```

**There are a number of methods available on string in python such as:**

- `.isalpha()`
- `.islower()`
- `.isupper()`
- `.isdigit()`
- `.endswith()`

The following block of code utilizes one such method: `isdigit()` to check if the house number entered is a digit or not.

```python
house_number = input("Please enter your house number")
    if house_number.isdigit():
        print("Thanks for sharing a valid house number")
    else:
        print("Invalid house number")
  ```
  
  ### More similar code
  
  ```python 
  salary = float(input("What is your salary? Please enter digits only"))
    print(f"Hi {first_name}, your salary is {salary}.")

    hobbies = input("What are your hobbies?")
    print(f"Hi {first_name}, thanks for sharing your hobbies, they are {hobbies}.")
    
 ```
   


### Create a gitignore file to ignore dependencies.
- Right click on the Python folder
- Click create a new file
- Name it as `.gitignore`
- Add all files to be ignored after an asterick. Eg `*./idea`


### Definition of Done

- Is a New Repository
- Is a New Project on Pycharm
- Has a READMe.md file
- Explains how to create a gitignore file
- Explains the code and the topics covered in the code
- Utilises the topics covered in the class
- Ignores dependencies that are not required to be pushed on GitHub
