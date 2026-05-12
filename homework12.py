student1 =int(input("Enter Jay age is : "))
student2 =int(input("Enter Viru age is : "))
student3 =int(input("Enter Gabbar age is : "))
if student1 >=0 and student2 >=0 and student3 >=0:
    if student1 >student2 and student1 >student3:
        print("jay is older than viru & Gabbar")
    elif student2 >student1 and student2 >student3:
        print("Viru is older than Jay & Gabbar")
    elif student3 >student1 and student3 >student2:
        print("Gabbar is older than jay & viru")
    else:
        print("two or more students have same age.")
else:
    print("Enter a Valid age ")