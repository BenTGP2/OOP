List = []

while True:
    print("1. Add an element to this list.")
    print("2. Remove an element from the list.")
    print("3. Replace an element in the list.")
    print("4. Sort the elements in the list.")
    print("5. Reverse the elements in the list")
    print("6. Print the elements in the list.")
    print("7. Exit program.")

    Option = input("What operation would you like to perform: ")
    if Option == "1":
        Input = input("Enter the value you would like to add:")
        List.append(Input)
        print(Input, "added.")
    elif Option == "2":
        Input = input("Enter the value you would like to remove:")
        List.remove(Input)
        print(Input, "removed.")
    elif Option == "3":
        print(List)
        Index = int(input("Enter the index of the value you would like to replace:"))
        Input = input("Enter the value you would like to swap in:")
        List[Index] = Input
    elif Option == "4":
        print("Sorting elements...")
        List.sort()
        print(List)
    elif Option == "5":
        print("Reversing elements...")
        List.reverse()
    elif Option == "6":
        print(List)
    elif Option == "7":
        print("Terminating program...")
        break
