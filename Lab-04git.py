class Customer:
    def __init__(self):
        self.name = ""
        self.ID = ""
        self.account_number = ""
        self.phone = ""
        self.email = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = []
    def add_values_to_customer(self):
        self.name = input("Enter the name of the customer: ")
        self.ID = input("Enter the ID of the customer: ")
        self.account_number = input("Enter the account number of the customer: ")
        self.phone = input("Enter the phone number of the customer: ")
        self.email = input("Enter the email of the customer: ")
        self.balance = float(input("Enter the balance of the customer: "))
    def display(self):
        print("The name of the customer is:", self.name)
        print("The account number is:", self.account_number)
        print("The phone number is:", self.phone)
        print("The email is:", self.email)
        print("The balance of the customer is:", self.balance)
        print("The account ID is:", self.ID)
        print("The credit card is:", self.credit_card)
        print("The debit card is:", self.debit_card)
    def withdraw(self, amount):
        self.balance -= amount
    def debit(self, amount):
        self.balance += amount
class Card:
    def __init__(self):
        self.type = ""
        self.number = ""
        self.exp_date = ""
        self.cvv = ""
        self.balance = 0.0
    def add_values_to_card(self):
        self.type = input("Enter the type of the card: ")
        self.number = input("Enter the number of the card: ")
        self.exp_date = input("Enter the exp date of the card: ")
        self.cvv = input("Enter the cvv of the card: ")
        self.balance = float(input("Enter the balance of the card: "))
    def display(self):
        print("The type of the card is:", self.type)
        print("The number of the card is:", self.number)
        print("The exp date of the card is:", self.exp_date)
        print("The cvv of the card is:", self.cvv)
        print("The balance of the card is:", self.balance)
c1 = Customer()
c2 = Customer()
p1 = Card()
p2 = Card()

while True:
    print("1. Add values to a customer")
    print("2. Add values to a card")
    print("3. Transfer customer balances")
    print("4. Register card with customer")
    print("5. Display customer info")
    print("6. Display card info")
    print("7. Commit")
    print("8. Exit program")

    Input = input("Enter your choice: ")
    if Input == "1":
        c1.add_values_to_customer()
        print("add values to the second customer: ")
        c2.add_values_to_customer()
    elif Input == "2":
        p1.add_values_to_card()
        print("Add values to the second card: ")
        p2.add_values_to_card()
    elif Input == "3":
        Choice = input("Enter the ID of the customer you would like to withdraw from: ")
        amount = float(input("Enter how much you want to withdraw: "))
        if Choice == c1.ID:
            c1.withdraw(amount)
            c2.debit(amount)
        elif Choice == c2.ID:
            c2.withdraw(amount)
            c1.debit(amount)
    elif Input == "4":
        CustomerChoice = input("Enter the ID of the customer you would like to register the card to: ")
        card_choice = input("Enter the number of the card you would like to register the user: ")
        if CustomerChoice == c1.ID:
            if card_choice == p1.number and p1.type == "credit":
                c1.credit_card.append(card_choice)
            elif card_choice == p1.number and p1.type == "debit":
                c1.debit_card.append(card_choice)
            elif card_choice == p2.number and p2.type == "credit":
                c1.credit_card.append(card_choice)
            elif card_choice == p2.number and p2.type == "debit":
                c1.debit_card.append(card_choice)
        elif CustomerChoice == c2.ID:
            if card_choice == p1.number and p1.type == "credit":
                c2.credit_card.append(card_choice)
            elif card_choice == p1.number and p1.type == "debit":
                c2.debit_card.append(card_choice)
            elif card_choice == p2.number and p2.type == "credit":
                c2.credit_card.append(card_choice)
            elif card_choice == p2.number and p2.type == "debit":
                c2.debit_card.append(card_choice)
    elif Input == "5":
        c1.display()
        c2.display()
    elif Input == "6":
        p1.display()
        p2.display()

