
x = int(input("enter a number 1"))
y = int(input("enter a number 2"))

while True:
    choice = int(input(
        "enter choice \n 1 for add \n 2 for subtract \n 3 for divide \n 4 for multiply \n 5 for remainder operation"))
    if choice == 1:
        result = x + y
        print("addition result ", result)
    elif choice == 2:
        result = x - y
        print("subtraction result ", result)
    elif choice == 3:
        if y == 0:
            print("division error")
        else:
            result = x/y
            print("division result ", result)
    elif choice == 4:
        result = x*y
        print("multiplication result ", result)
    elif choice == 5:
        if y == 0:
            print("division error")
        else:
            result = x%y
            print("remainder operation result ", result)
    else:
        print("invalid choice")
        quit()

