money = float(input("Enter Money: "))

def calculate_change():
    calculationmoney = money * 100
    ten_dollar = 1000
    five_dollar = 500
    one_dollar = 100
    quarter = 25
    dime = 10
    nickle = 5
    penny = 1
    amount = 0

    while calculationmoney >= ten_dollar:
        calculationmoney -= ten_dollar
        amount += 1
    print("x", amount, "$10 bill due.")
    amount = 0
    while calculationmoney >= five_dollar:
        calculationmoney -= five_dollar
        amount += 1
    print("x", amount, "$5 bill due.")
    amount = 0
    while calculationmoney >= one_dollar:
        calculationmoney -= one_dollar
        amount += 1
    print("x", amount, "$1 bill due.")
    amount = 0
    while calculationmoney >= quarter:
        calculationmoney -= quarter
        amount += 1
    print("x", amount, "Quarter due.")
    amount = 0
    while calculationmoney >= dime:
        calculationmoney -= dime
        amount += 1
    print("x", amount, "Dime due.")
    amount = 0
    while calculationmoney >= nickle:
        calculationmoney -= nickle
        amount += 1
    print("x", amount, "Nickle due.")
    amount = 0
    while calculationmoney >= penny:
        calculationmoney -= penny
        amount += 1
    print("x", amount, "Penny due.")

calculate_change()
