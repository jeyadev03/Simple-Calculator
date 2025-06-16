print("Welcome to Python Calculator!")
Num1=int(input("Enter the first number: "))
Num2=int(input("Enter the second number: "))
Operation=input("Choose an Operation(+,-,*,/): ")
if Operation == "+":
    result = Num1 + Num2
elif Operation == "-":
    result = Num1 - Num2
elif Operation == "*":
    result = Num1 * Num2
elif Operation == "/":
    if Num2!=0:
        result = Num1 / Num2
    else:
        result = "Error : Division by zero is not allowed"
else:
    result = "Invalid Operation"

print("Result:",result)    
