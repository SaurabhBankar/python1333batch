v1 = input("Enter a number:")
print("you entered:", v1)
print("type of v1:", type(v1))
print("memory address of v1:", id(v1))

#we can convert the string to an integer using the int() function
v2=int(v1)
print("v2:", v2)
print("type of v2:", type(v2))
print("memory address of v2:", id(v2))

v1=int(input("Enter a number:"))
print("you entered:", v1)
print("type of v1:", type(v1))

jay=23
viru=23
if jay>viru:
    print("jay will pay bill")
else:
    print("viru will pay bill")