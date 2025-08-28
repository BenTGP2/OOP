EmployeeName = input("Please enter your name: ")
HourlyWage = float(input("Enter your hourly wage: "))
HoursWorked = float(input("Enter your hours worked per day: "))
DaysWorked = int(input("Enter your days worked this Month: "))

MonthlyWage = HourlyWage*HoursWorked*DaysWorked

print(EmployeeName," has made $", MonthlyWage, " this Month!")