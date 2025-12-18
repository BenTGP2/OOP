#save customer history
#finish GUI

import pickle
import json
import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk



from datetime import date
currentDay = date.today()
str(currentDay)

History = {}
Cart = []

customerNum = 1



class User:
    def __init__(self):
        self.Cid = ""
        self.PaymentType = ""
        self.Member = ""

    def add_values(self):
        self.Cid = input("Please enter a unique Customer ID: ")
        self.PaymentType = input("Enter Chosen Payment Type: ")
        self.Member = input("Membership Status: ")

class Admin:
    def __init__(self):
        self.Aid = ""
        self.Name = ""
        self.Password = ""

    def add_values(self):
        self.Aid = input("Please enter a unique Admin ID: ")
        self.Name = input("Please enter the Admin's Name: ")
        self.Password = input("Please enter a new Password: ")

    def save(self):
        with open("admin.dat", "ab") as file1:
            pickle.dump(self, file1)
        file1.close()

print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
print("Welcome to the Burger Shack Menu Manager!")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

tax = .08
global loggedIn
loggedIn = False

Menu = {
    "i1": {"Name": "Burger", "Price": 7.50, "Desc": "A delicious burger.", "PosX": 100, "PosY": 100},
    "i2": {"Name": "Fries", "Price": 3.00, "Desc": "Crispy fries.", "PosX": 100, "PosY": 300},
    "i3": {"Name": "Soda", "Price": 1.50, "Desc": "Refreshing soda.","PosX": 100, "PosY": 500}
}

def login(x):
    aID = input("Please enter your Admin ID: ")
    Password = input("Please enter your Admin Password: ")
    f2 = open("admin.dat", "rb")
    working = False

    while 1:
        try:
            data = pickle.load(f2)

            if aID == data.Aid and Password == data.Password:
                working = True
                x = True
                loggedIn = x
                return x

        except EOFError:
            break

    if working:
        print("Logging In As: ", data.Name)
        print(loggedIn)

    else:
        print("Incorrect Login Credentials")

def print_menu():
    for menu_items in Menu.items():
        print(menu_items)
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

def add_to_cart():
    Var = input("Please enter the ID of the item selected: ")

    itemAdd = Menu[Var]
    Cart.append(itemAdd)

    print(Cart)

def remove_from_cart():
    Var = input("Please enter the ID of the item you wish to remove: ")

    itemAdd = Menu[Var]
    Cart.remove(itemAdd)

    print(Cart)

def save_menu():
    with open("menu.dat", "wb") as file1:
        pickle.dump(Menu, file1)
    file1.close()

def save_history():
    with open("purchase_logs.dat", "ab") as file2:
      pickle.dump(History, file2)
    file2.close()

def load_history():
    with open("purchase_logs.dat", "rb") as file1:
        Logs = pickle.load(file1)
        print(Logs)
    file1.close()

def setup_ui():
    for item_id, item_data in Menu.items():
        print(f"ID: {item_id}")
        print(f"Name: {item_data['Name']}")
        print(f"Price: {item_data['Price']}")
        print(f"Description: {item_data['Desc']}")


def open_checkout_window():
    checkout_win = Toplevel()
    checkout_win.title("Checkout")
    checkout_win.geometry("300x150")

    label = Label(checkout_win, text="Enter amount paid:", font=("ComicSans", 14))
    label.pack(pady=10)

    amount_entry = Entry(checkout_win, font=("ComicSans", 12))
    amount_entry.pack(pady=5)

    def process_payment():
        try:
            paid_amount = float(amount_entry.get())
            process_purchase_with_payment(paid_amount, change_due_var)
            checkout_win.destroy()
        except ValueError:
            print("Please enter a valid number.")

    submit_btn = Button(checkout_win, text="Submit Payment", command=process_payment, font=("ComicSans", 12))
    submit_btn.pack(pady=10)

def process_purchase_with_payment(paid_amount, change_label_var):
    total = sum(item["Price"] for item in Cart)
    PostTaxTotal = total * (1 + tax)
    toReturn = paid_amount - PostTaxTotal
    print("Total due: $%.2f" % PostTaxTotal)
    print("Amount paid: $%.2f" % paid_amount)
    print("Change to return: $%.2f" % toReturn)

    # Update label
    change_label_var.set(f"Change Due After Tax: ${toReturn:.2f}")

    if toReturn >= 0:
        calculationmoney = toReturn * 100
        fifty_dollar = 5000
        twenty_dollar = 2000
        ten_dollar = 1000
        five_dollar = 500
        one_dollar = 100
        quarter = 25
        dime = 10
        nickle = 5
        penny = 1
        amount = 0

        while calculationmoney >= fifty_dollar:
            calculationmoney -= fifty_dollar
            amount += 1
        print("x", amount, "$50 bill due.")
        amount = 0
        while calculationmoney >= twenty_dollar:
            calculationmoney -= twenty_dollar
            amount += 1
        print("x", amount, "$20 bill due.")
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

        Purchases = str(Cart)

        History.update({currentDay: {
            "Customer Number": customerNum,
            "Purchases": Purchases
        }})
        print(History)
        customerNum + 1
        save_history()
    else:
        print("Insufficient payment.")

def ui_create():
    global change_due_var, CartList, total_price_var, CustomerNum
    # User Interface Setup
    BurgerUI = Tk()
    BurgerUI.geometry("1920x1080")

    MenuTitle = tk.Label(text="MENU ITEMS", font=("ComicSans", 20, "bold"))
    MenuTitle.place(x=120, y=10)

    CartList = tk.Text(BurgerUI, width=50, height=25)
    CartList.place(x=1375, y=50)

    CartTitle = tk.Label(text="ITEMS IN CART", font=("ComicSans", 20, "bold"))
    CartTitle.place(x=1475, y=10)

    RemoveTitle = tk.Label(text="Remove Item", font=("ComicSans", 20, "bold"))
    RemoveTitle.place(x=1500, y=550)

    CustomerTitle = tk.Label(text=(f"Customer Number:"), font=("ComicSans", 20, "bold"))
    CustomerTitle.place(x=1000, y=50)

    CustomerNum = tk.Label(text=customerNum, font=("ComicSans", 20, "bold"))
    CustomerNum.place(x=1300, y=50)

    ready_checkout_btn = tk.Button(BurgerUI, text="Ready to Checkout", font=("ComicSans", 16, "bold"),command=open_checkout_window)
    ready_checkout_btn.place(x=1500, y=750)

    change_due_var = tk.StringVar()
    change_due_var.set("Change Due After Tax: $0.00")
    change_due_label = tk.Label(BurgerUI, textvariable=change_due_var, font=("ComicSans", 16, "bold"))
    change_due_label.place(x=1450, y=800)

    def remove_item():
        try:
            index = int(RemoveInput.get("1.0", "end-1c").strip()) - 1
            if 0 <= index < len(Cart):
                removed_item = Cart.pop(index)
                print(f"Removed: {removed_item['Name']} from cart.")
                CartList.delete("1.0", END)
                for idx, itm in enumerate(Cart, 1):
                    CartList.insert(END, f"{idx}. {itm['Name']} - ${itm['Price']}\n")
                update_total()
            else:
                print("Invalid number. Please enter a valid item number.")
        except ValueError:
            print("Please enter a valid number.")

    RemoveInput = tk.Text(BurgerUI, width=10, height=1)
    RemoveInput.place(x=1550, y=600)

    btn_remove = tk.Button(BurgerUI, text="Remove", font=("ComicSans", 14, "bold"), command=remove_item)
    btn_remove.place(x=1550, y=650)

    total_price_var = tk.StringVar()
    total_price_var.set("Total Before Tax: $0.00")
    TotalPriceLabel = tk.Label(BurgerUI, textvariable=total_price_var, font=("ComicSans", 20, "bold"))
    TotalPriceLabel.place(x=1450, y=475)


    def update_total():
        total = sum(item["Price"] for item in Cart)
        total_price_var.set(f"Total Before Tax: ${total:.2f}")

    def add_item_to_cart(item_id):
        print(f"Attempting to add item with ID: {item_id}")
        if item_id not in Menu:
            print(f"Error: '{item_id}' not found in Menu.")
            return
        item = Menu[item_id]
        Cart.append(item)
        CartList.delete("1.0", END)
        for idx, itm in enumerate(Cart, 1):
            CartList.insert(END, f"{idx}. {itm['Name']} - ${itm['Price']}\n")
        update_total()

    def reset_all():
        global Cart, customerNum
        Cart.clear()
        CartList.delete("1.0", END)
        change_due_var.set("Change Due After Tax: $0.00")
        total_price_var.set("Total Before Tax: $0.00")
        customerNum += 1
        CustomerNum.config(text=str(customerNum))

    next_customer = tk.Button(BurgerUI, text="Next Customer", font=("ComicSans", 14, "bold"), command=reset_all)
    next_customer.place(x=1100, y=100)
    #Menu Items
    #def create_item_ui():
        #for item_id, item_data in Menu.items():
            #print(f"ID: {item_id}")
            #print(f"Name: {item_data['Name']}")
            #print(f"Price: {item_data['Price']}")
            #print(f"Description: {item_data['Desc']}")

            #ItemLabel = tk.Label(text=item_data["Name"], width=200,height=200)
            #ItemLabel.place(x=item_data["PosX"],y=item_data["PosY"])
            #ItemPrice = tk.Label(text=item_data["Price"], width=100,height=100)
            #ItemPrice.place(x=item_data["PosX"]+100,y=item_data["PosY"])
    #create_item_ui()



    #Item 1: Hamburger
    ImagePath = Image.open('Hamburger.png')
    Item1Image = ImagePath
    Item1_tk_image = ImageTk.PhotoImage(Item1Image)
    HamburgerImageLabel = Label(BurgerUI, image=Item1_tk_image, width=200, height=200)
    HamburgerImageLabel.place(x=100, y=50)
    HamburgerImageLabel.image = Item1_tk_image

    btn_hamburger = tk.Button(BurgerUI, text="Add Hamburger", font=("ComicSans", 14, "bold"), command=lambda: add_item_to_cart("i1"))
    btn_hamburger.place(x=350, y=50)

    price_hamburger = Menu.get("i1", {}).get("Price", 0)
    lbl_price_hamburger = tk.Label(BurgerUI, text=f"Price: ${price_hamburger:.2f}", font=("ComicSans", 14))
    lbl_price_hamburger.place(x=350, y=100)

    # Item 2: Fries
    ImagePath = Image.open('Fries.png')
    FriesImage = ImagePath
    Fries_tk_image = ImageTk.PhotoImage(FriesImage)
    FriesImageLabel = Label(BurgerUI, image=Fries_tk_image, width=200, height=200)
    FriesImageLabel.place(x=100, y=300)
    FriesImageLabel.image = Fries_tk_image

    btn_fries = tk.Button(BurgerUI, text="Add Fries", font=("ComicSans", 14, "bold"), command=lambda: add_item_to_cart("i2"))
    btn_fries.place(x=350, y=300)

    price_fries = Menu.get("i2", {}).get("Price", 0)
    lbl_price_fries = tk.Label(BurgerUI, text=f"Price: ${price_fries:.2f}", font=("ComicSans", 14))
    lbl_price_fries.place(x=350, y=350)

    #Item 3: Soda
    ImagePath = Image.open('Soda.png')
    SodaImage = ImagePath
    Soda_tk_image = ImageTk.PhotoImage(SodaImage)
    SodaImageLabel = Label(BurgerUI, image=Soda_tk_image, width=200, height=200)
    SodaImageLabel.place(x=100, y=550)
    SodaImageLabel.image = Soda_tk_image

    btn_soda = tk.Button(BurgerUI, text="Add Soda", font=("ComicSans", 14, "bold"), command=lambda: add_item_to_cart("i3"))
    btn_soda.place(x=350, y=550)

    price_soda = Menu.get("i3", {}).get("Price", 0)
    lbl_price_soda = tk.Label(BurgerUI, text=f"Price: ${price_soda:.2f}", font=("ComicSans", 14))
    lbl_price_soda.place(x=350, y=600)

    BurgerUI.mainloop()
#Menu Loader
while 1:
    updateMenu = input("Would you like to load the preset menu? y/n: ")

    if updateMenu == "y":

        print("Loading preset menu!")

        with open("menu.dat", "rb") as file1:
            Menu = pickle.load(file1)

        file1.close()

        print_menu()
        # itemID = "i1"
        # Name = "Burger"
        # Price = 7.50
        # Desc = "A medium well slow cooked burger."
        #
        # Menu.update({itemID: {
        #     "Item": Name,
        #     "Price": Price,
        #     "Description": Desc
        # }})
        #
        # itemID = "i2"
        # Name = "Fries"
        # Price = 3.00
        # Desc = "A large bag of steak fries."
        #
        # Menu.update({itemID: {
        #     "Item": Name,
        #     "Price": Price,
        #     "Description": Desc
        # }})
        #
        # itemID = "i3"
        # Name = "Soda"
        # Price = 1.50
        # Desc = "A 16oz fountain drink."
        #
        # Menu.update({itemID: {
        #     "Item": Name,
        #     "Price": Price,
        #     "Description": Desc
        # }})
        #
        # print("Displaying Current Menu!")
        # print("")
        # print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        #
        # print_menu()
        #
        # print("")
        # print("Loading Program!")

        break

    elif updateMenu == "n":
        print("Loading Program!")
        break

    else:
        print("Invalid Command Received!")

#Login Loop
while 1:
    if loggedIn == False:
        print("Would you like to login?")
        opt = input("y/n: ")

        if opt == "y":
            adminVar = Admin()
            loggedIn = login(False)
            break
        elif opt == "n":
            break
        else:
            print("Error")
    else:
        break

#Main Loop
while 1:
    #Check if user is admin or customer
    if loggedIn == False:
        print("[1] Proceed To Checkout")
        print("[2] View Menu")
        print("[3] Add Items To Cart")
        print("[4] View / Remove Items From Cart")
        print("[Q] Quit")

    elif loggedIn == True:
        print("[1] Modify Menu Items")
        print("[2] Change Data")
        print("[3] Save Menu File")
        print("[4] Add Items to Menu")
        print("[5] Manage Users")
        print("[6] View Customer History")
        print("[7] Open UserInterface")#

        setup_ui()

    opt = input("Please enter your selection: ")



    if opt == "1":
        print("Input Received!", "[", opt, "]")

        print_menu()

        iID = input("Enter the ItemID: ")
        name = input("Enter the Item's new name: ")
        price = float(input("Enter the Item's new price: "))
        desc = input("Enter the Item's new description: ")

        Menu.update({iID: {
            "Name": name,
            "Price": price,
            "Desc": desc
        }})

        print("Item Modified!")

    elif opt == "2":
        print("Input Received!", "[", opt, "]")
        print("Current Tax: ", 100 * tax, "%")
        opt = input("Change Tax Rate? y/n: ")

        while 1:
            if opt == "y":
                tax = float(input("Please enter the new tax percentage: "))

                if tax < 1:
                    print("Current Tax: ", 100 * tax, "%")
                elif tax > 1:
                    print("Current Tax: ", tax, "%")
                    newTax = tax/100

                    tax = newTax
                elif tax == 1:
                    print("Current Tax: ", 100 * tax, "%")
                else:
                    print("Invalid Tax")
                break

            elif opt == "n":
                print("Returning to menu")
                break

            else:
                print("Invalid input")
                break

    elif opt == "3":
        print("Saving Menu!")
        save_menu()
        print("Saved Successfully!")

    elif opt == "4":
        print("Input Received!", "[", opt, "]")

        print_menu()

        iID = input("Enter a new ItemID: ")
        name = input("Enter the Item's name: ")
        price = float(input("Enter the Item's price: "))
        desc = input("Enter the Item's description: ")

        Menu.update({iID: {
            "Name": name,
            "Price": price,
            "Desc": desc
        }})

        print("Item Added!")

    elif opt == "5":
        while 1:
            print("[1] Add New Admin User")
            print("[2] Add New Customer")
            print("[3] Delete Customer")
            print("[4] Quit")

            opt = input("Enter your selection: ")

            if opt == "1":
                adminVar = Admin()
                adminVar.add_values()
                adminVar.save()

            elif opt == "2":
                userVar = User()
                userVar.add_values()

            elif opt == "3":
                userVar = User()
                userVar.__delattr__("Cid")
                userVar.__delattr__("PaymentType")
                userVar.__delattr__("Member")

            elif opt == "4":
                break

            else:
                print("Error")

    elif opt == "6":
        print("Loading History!")
        load_history()

    elif opt == "7":
        print("Loading Interface!")
        ui_create()

    else:
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        print("Invalid Input Received!", "[", opt, "]")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")