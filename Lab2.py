EmployeeDictionary = {}

while True:
    print("1. Register new employee")
    print("2. Remove existing employee")
    print("3. Edit existing employee")
    print("4. List all employees")
    print("5. Exit program")

    Input = input("Select option: ")

    if Input == "1":
        EmployeeID = input("Enter employee ID: ")
        EmployeeName = input("Enter employee name: ")
        EmployeeWage = float(input("Enter employee wages: "))
        Allowance = float(input("Enter allowance: "))
        Deduction = float(input("Enter deduction: "))
        Taxes = float(input("Enter taxes: "))
        NetPay = EmployeeWage+Allowance
        GrossPay = NetPay-(Deduction+Taxes)

        EmployeeDictionary.update({EmployeeID:{
            "Name":EmployeeName,
            "Wages":EmployeeWage,
            "Allowance":Allowance,
            "Deduction":Deduction,
            "Taxes":Taxes,
            "NetPayment":NetPay,
            "GrossPayment":GrossPay
            }
        })
    elif Input == "2":
        Removing = input("Enter the ID of the employee whose information you would like to remove: ")
        del EmployeeDictionary[Removing]
        print("Removed", Removing)
    elif Input == "3":
        Replacing = input("Enter the SID of the student whose information you would like to replace: ")
        del EmployeeDictionary[Replacing]

        print("Enter updated information.")

        EmployeeID = input("Enter new employee ID: ")
        EmployeeName = input("Enter new employee name: ")
        EmployeeWage = float(input("Enter new employee wages: "))
        Allowance = float(input("Enter new allowance: "))
        Deduction = float(input("Enter new deduction: "))
        Taxes = float(input("Enter new taxes: "))
        NetPay = EmployeeWage+Allowance
        GrossPay = NetPay-(Deduction+Taxes)

        EmployeeDictionary.update({EmployeeID:{
            "Name":EmployeeName,
            "Wages":EmployeeWage,
            "Allowance":Allowance,
            "Deduction":Deduction,
            "Taxes":Taxes,
            "NetPayment":NetPay,
            "GrossPayment":GrossPay
            }
        })
    elif Input == "4":
        for EmployeeRecord in EmployeeDictionary.items():
            print(EmployeeRecord)
            print("---------------------------------------------------------------------------------------------------")
    elif Input == "5":
        print("Terminating program...")
        break



