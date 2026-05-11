roll = 3
name = "saurabh"
per = 90.23455
# s = "Student roll is" + str(roll) + "and name is" + name 
s=f"student roll is {roll:03d} and name is {name}. Percentage is {per:.2f}."  #f string method
print(s)
s1="student roll is {} and name is {}. Percentage is {}." .format(roll,name,per )  #.format string method
print(s1)
s2="student roll is {0} and name is {1}. Percentage is {2}." .format(roll,name,per )  #.format string method
print(s2)
s3="student roll is {v1} and name is {v2}. Percentage is {v3}." .format(v1=roll,v2=name,v3=per )  #.format string method
print(s3)
s1="student roll is %d and name is %s. Percentage is %.2f." %(roll,name,per )  #.% string method
print(s1)

print("-"*40)

print("|Roll | Name | Percentage")  #table header format
print("-"*40)
print(f"|{roll:<6} |{name:^5} |{per:>10}")
print("-"*40)

filename =input("Enter file name: ")
path = f"C:\\Users\\saurabh\\Desktop\\{filename}"
print(path)