Student=input("Enter student name: ")
marks=int(input("Enter marks: "))
percentage=float(input("Enter percentage: "))
print(f"{Student} scored {marks} with percentage {percentage:.2f}%")
print("{Student} scored {marks} with percentage {percentage:.2f}%".format(Student=Student, marks=marks, percentage=percentage))
print("%s scored %d with percentage %d%%" % (Student, marks, percentage))


age=int(input("Enter age: "))
after_age=age+10
print(f"Your age after 10 years will be {after_age} years.")
print("Your age after 10 years will be {after_age} years.".format(after_age=after_age))
print("Your age after 10 years will be %d years." % after_age)


student1=input("Enter student name: ")
marks1=int(input("Enter marks: "))
student2=input("Enter student name: ")
marks2=int(input("Enter marks: "))
student3=input("Enter student name: ")
marks3=int(input("Enter marks: "))
print("Student Name | Marks")  #table header format
print("-"*30)
print(f"{student1:<12} | {marks1:>5}")
print("-"*30)
print(f"{student2:<12} | {marks2:>5}")
print("-"*30)
print(f"{student3:<12} | {marks3:>5}")
print("-"*30)


student_name=input("Enter student name: ")
subejct1=input("Enter subject 1 name: ")
marks1=int(input("Enter marks for subject 1: "))
subejct2=input("Enter subject 2 name: ")
marks2=int(input("Enter marks for subject 2: "))
subejct3=input("Enter subject 3 name: ")
marks3=int(input("Enter marks for subject 3: "))
subject4=input("Enter subject 4 name: ")
marks4=int(input("Enter marks for subject 4: "))
subject5=input("Enter subject 5 name: ")
marks5=int(input("Enter marks for subject 5: "))
total_marks=marks1+marks2+marks3+marks4+marks5
Grade=""
if total_marks>=400:
    Grade="A"
elif total_marks>=300:
    Grade="B"
elif total_marks>=200:
    Grade="C"
elif total_marks>=100:
    Grade="D"
else:
    Grade="F"
print("\n")
print("The Kiran Academy Report card")
print("-"*30)
print("Student Name: ", student_name)
print("="*30)
print(f"Subject Name | {'Marks':^8}")
print("="*30)
print(f"{subejct1:<12} | {marks1:>5}")
print("-"*30)
print(f"{subejct2:<12} | {marks2:>5}")
print("-"*30)
print(f"{subejct3:<12} | {marks3:>5}")
print("-"*30)
print(f"{subject4:<12} | {marks4:>5}")
print("-"*30)
print(f"{subject5:<12} | {marks5:>5}")
print("="*30)
print(f"Total Marks: {total_marks}")
print("-"*30)
print(f"Grade: {Grade}")