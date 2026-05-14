Jay = 21
viru = 21

if Jay > viru:
    print("Jay is pay the bill")
elif Jay == viru:
    print("Jay and Viru will pay the bill")
else :
    print("Viru is pay the bill")

print("------------PUNE RTO Driving License Test Application------------")
age=int(input("Enter your age: "))
age1= 18
cal =  age1 - age  #calculation for how many years left to apply for a driving license
if age >= 18 and age <= 75:
    print("You are eligible to apply for a driving license.")
elif age < 18:
    print("You are not eligible to apply for a driving license." "Wait for",cal,"years to apply.") #used the calculation to show how many years left to apply for a driving license
else:
    print("Your age is Bar.")