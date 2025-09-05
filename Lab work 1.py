while True:
    print("Please Select an Operation.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit Program")

    Selected = input("Enter your selected operation: ")

    if Selected == "1":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        Answer = Num1 + Num2
        print("The answer is: ", Answer)
    elif Selected == "2":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        Answer = Num1 - Num2
        print("The answer is: ", Answer)
    elif Selected == "3":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        Answer = Num1 * Num2
        print("The answer is: ", Answer)
    elif Selected == "4":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        Answer = Num1 / Num2
        print("The answer is: ", Answer)
    elif Selected == "5":
        break
print("Thank you for using my program, goodbye!")
