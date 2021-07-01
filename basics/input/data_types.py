print("What is your name Human?")
name = input ()
print("How old are you(in years)?")
#when you use input the defaul data type is a string and needs to be transformed into a number 
age = int(input ())
print("How tall are you (in meters)?")
#for numbers with a decimal number you use float
height = float(input())
print("How much do you weight (in Kilograms)?")
weight = float(input())
bmi = weight/(height **2)
print("{} you are {}years old and your bmi is {}".format(name,age,bmi))