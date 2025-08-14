#swapping 2 number without using 3rd variable

a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
print("\n Before Swapping")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("After Swapping: a=",a,"b=",b)