Height = float(input("Enter Height(cm): "))
Weight = float(input("Enter Weight(Kg): "))

Height = Height/100
BMI = Weight/(Height*Height)
print("your Body Mass Index: ", BMI)

if(BMI > 0):
    if(BMI <= 16):
        print("You are Severely Underweight")
    elif(BMI <= 18.5):
        print("You are Underweight")
    elif(BMI <= 25):
        print("You are Healthy")
    elif(BMI <= 30):
        print("You are Overweight")
    else:
        print("You are Severely Overweight")
else:
    ("Enter Valid Details")
