def calculator_bmi():
    print("it is bmi calculator")
    try:
        #get user input for weight and height
        weight=float(input("enter your weight in kilograms"))
        height=float(input("enter your height in meters"))
        #bmi calculation
        bmi=weight/(height**2)
        #display bmi value

        print(f"your BMI is:{bmi:.2f}")
        #interpret the bmi value
        if bmi<=18.5:
            print("you are underweight")
        elif 18.5<= bmi <24.9:
            print("you have a normal weight")
        elif 25<= bmi <29.9:
            print("you are overweight")
        else:
            print("you are obese")
    except ValueError:
        print("invalid input! please enter numeric values for height")
calculator_bmi()
        
