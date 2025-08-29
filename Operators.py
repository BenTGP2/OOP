Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))

print("Operations will be performed with Num1 as the recipient.")

Operator = input("What operation would you like to perform: ")

if Operator == "+":
    Solution = Num1 + Num2
    print("The addition result is: ", Solution)
elif Operator == "-":
    Solution = Num1 - Num2
    print("The subtraction result is: ", Solution)
elif Operator == "*":
    Solution = Num1 * Num2
    print("The multiplication result is: ", Solution)
elif Operator == "/":
    Solution = Num1 / Num2
    print("The division result is: ", Solution)
