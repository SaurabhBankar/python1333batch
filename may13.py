Name = input("Enter employee name : ")
print("="*30)
Basic_salary=int(input("Enter basic salary : "))
print("="*30)
HRA=Basic_salary*0.10     #Formula for HRA of 10%
print("HRA is :10% ",HRA)
print("="*30)
DA=Basic_salary*0.20     #Formula for DA of 20%
print("DA is :20% ",DA)
print("="*30)
PF=Basic_salary*0.12     #formula for PF of 12%
print("PF is :12% ",PF)    
print("="*30)
Net_salary=Basic_salary+HRA+DA-PF  #formula for Calculating Net Salary
print("Net Salary is : ",Net_salary)
print("="*30)

Name = input("Enter employee name : ")
print("="*30)
Basic_salary=int(input("Enter basic salary : "))
print("="*30)
HRA=Basic_salary*0.10     #Formula for HRA of 10%
DA=Basic_salary*0.20     #Formula for DA of 20%
PF=Basic_salary*0.12     #formula for PF of 12%
Net_salary=Basic_salary+HRA+DA-PF  #formula for Calculating Net Salary
print(f"{'HRA':^7} | {'DA':^8} | {'PF':^7} | {'Net Salary':<7}")  #table header format
print("-"*40)
print(f"{HRA:>5.2f} | {DA:>5.2f} | {PF:>5.2f} | {Net_salary:>10.2f}")
print("-"*40)