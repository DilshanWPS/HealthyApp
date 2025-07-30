def NameValid(prompt):
    while True:
        name = input(prompt).strip()
        if not name:
            print(" Name cannot be empty.")
        elif name.replace(" ", "").isalpha():
            return name
        else:
            print("Please enter a valid name (letters only).")

def InputValid(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(" Please enter a positive number.")
            else:
                return value
        except ValueError:
            print(" Invalid input. Please enter a number.")

def AgeValid(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print(" Please enter a valid age above 0.")
            else:
                return value
        except ValueError:
            print(" Invalid input. Please enter a whole number.")

def genderValid(prompt):
    while True:
        gender = input(prompt).strip().lower()
        if gender in ["male", "female"]:
            return gender
        else:
            print(" Please enter 'male' or 'female'.")

def ActivityValid():
    
    valid_options = {"1", "2", "3", "4", "5"}

    while True:
        choice = input("Enter activity level (1–5): ").strip()
        if choice in valid_options:
            return choice
        else:
            print(" Invalid choice. Please enter a number between 1 and 5.")
