def CalcBmr(gender, weight, height, age):
    gender = gender.lower()
    if gender == "male":
        return round(10 * weight + 6.25 * height - 5 * age + 5, 2)
    else:
        return round(10 * weight + 6.25 * height - 5 * age - 161, 2)
   