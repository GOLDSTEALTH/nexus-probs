# EMPLOYEE REGISTRATION SOFTWARE

name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
salary = float(input("Enter your Salary : "))
Policy_Accepted = bool(input("Have you accepted the company policy? (True/False) : "))

Emp_id = name[:3]
first_letter_ASCII = ord(name[0]) if name else None

print ("your Name : ", name)
print ("your Age : ", age)
print ("your Salary : ", salary)
print ("Policy Accepted : ", Policy_Accepted)
print ("Employee ID : ", Emp_id)
print ("First Letter ASCII : ", first_letter_ASCII)