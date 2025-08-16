num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
temp=num1
num1=num2
num2=temp
print(num1)
print(num2)

#shortcut swap without using 3 varible

num1=int(input("Enter the num1"))
num2=int(input("Enter the num2:"))
num1,num2=num2,num1
print(num1)
print(num2)

#with 3 variables

num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
num3=int(input("Enter the num3:"))
print("Before swapping:" ,num1,num2,num3)
num1,num2,num3=num3,num2,num1
print("After swaping:",num1,num2,num3)