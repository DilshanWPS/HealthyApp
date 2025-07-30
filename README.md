HealthyCalc

    HealthyCalc is a simple Python-based Health Calculator that calculates:
    - BMI (Body Mass Index)
    - BMR (Basal Metabolic Rate)
    - Daily Calorie Needs
    - Suggested Daily Water Intake


    Features

    - Input validation (name, age, weight, height, gender, activity level)
    - Clean modular design with reusable components
    - Activity-based calorie multiplier
    - Friendly console interface

    Folder structure
     
    HealthyCalc
    │
    ├── HealthyCalc/ # Package folder
    │├──__init__.py
    │├── activity.py # Activity level multiplier
    │├──bmi.py # BMI calculation and category
    │├── bmr.py # BMR calculation
    │├── inputValidate.py # User input validation
    │└── water.py # Water intake calculation
    │
    ├── main.py # Main program entry point
    └── README.md # Project info and usage

    How to Run the Project

    1. Clone the repository

        git clone https://github.com/your-username/HealthyCalc.git
        cd HealthyCalc

    2.Make sure Python is installed

        python --version
        If not installed, download it from: https://www.python.org/downloads/
    
    3.Run the program

        python main.py
        Follow the displayed instructions
    