from HealthyCalc.inputValidate import NameValid, InputValid, AgeValid, genderValid, ActivityValid
from HealthyCalc.bmi import CalculateBmi, BmiCategory
from HealthyCalc.bmr import CalcBmr
from HealthyCalc.activity import ActMultiplier
from HealthyCalc.water import CalcWater

def main():
    print("Welcome to the Health Calculator!\n")

    name = NameValid("Enter your name: ")
    age = AgeValid("Enter your age(years): ")
    gender = genderValid("Enter your gender (male/female): ")
    weight = InputValid("Enter your weight in kg: ")
    height = InputValid("Enter your height in cm: ")

    print("\nChoose your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise 1–3 days/week)")
    print("3. Moderately active (moderate exercise 3–5 days/week)")
    print("4. Very active (hard exercise 6–7 days/week)")
    print("5. Super active (very hard exercise, physical job)")

    activity_level = ActivityValid()

    bmi = CalculateBmi(weight, height)
    bmi_status = BmiCategory(bmi)
    bmr = CalcBmr(gender, weight, height, age)
    multiplier = ActMultiplier(activity_level)
    daily_calories = round(bmr * multiplier, 2)
    water_intake = CalcWater(weight)

    print(f"\n{name}, here are your results:")
    print(f"BMI: {bmi} ({bmi_status})")
    print(f"BMR: {bmr} calories/day")
    print(f"Total Daily Calorie Needs: {daily_calories} calories/day")
    print(f"Suggested Water Intake: {water_intake} liters")

if __name__ == "__main__":
    main()
