choice=int(input("Press 1 for celsius to Fahrenheit: or Press 2 for F to c:"))
if choice==1:
    celsius=float(input("Enter the tempe to convert it in celsius"))
    fahrenheit=(celsius*9/5)+32
    print("Temperature in Fahrenheit:",fahrenheit)
elif choice==2:
    fahrenheit=float(input("Enter the temp in fahrenheit"))
    celsius=(fahrenheit-32)*5/9
    print("Temperature in celsius",celsius)
else:
    print("Invalid choice")
