# user_details

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
 It then prints back the first, middle and last name after concatinating them.
 This method of concatination id called *formatted string literal* or *f-string*
 
There are other methods of concatination like using a `+` symbol.
```python
print(first_name + " " + mid_name+ " " + last_name+ " " +str(age))
```


### Create a gitignore file to ignore dependencies.
- Right click on the Python folder
- Click create a new file
- Name it as `.gitignore`
- Add all files to be ignored after an asterick. Eg `*./idea`
