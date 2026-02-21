database = []

def table():
    row = int(input(f"Row: "))
    col = int(input(f"Column: "))

    for i in range(row):
        rows = []
        database.append(rows)
        for j in range(col):
            rows.append(None)
    
    print(f"Table created")

def insert_value():
    r = int(input(f"Enter the rows: "))
    c = int(input(f"Enter the cols: "))
    v = input("Enter: ")
    
    if 0 <= r < len(database) and 0 <= c < len(database[0]):
        if database[r][c] is None:
            database[r][c] = v
            print("Inserted")
        else:
            print("Cell already filled (use edit)")
    else:
        print("Invalid index ")

def edit():
    r1 = int(input(f"Enter the rows: "))
    c1 = int(input(f"Enter the cols: "))
    v1 = input("Enter: ")
    
    if 0 <= r1 < len(database) and 0 <= c1 < len(database[0]):
        database[r1][c1] = v1
        print("Updated")
    else:
        print("Invalid index")

def view():
    print("Database:")
    for row in database:
        print(row)

def remove():
    r2 = int(input(f"Enter the rows: "))
    # c2 = int(input(f"Enter the cols: "))

    database.pop(r2)

def search():
    r = int(input(f"Enter the rows: "))
    c = int(input(f"Enter the cols: "))
    if 0 <= r < len(database) and 0 <= c < len(database[0]):
        print(f"Value: {database[r][c]}")
    else:
        print("Invalid index")

def menu():
    while True:
        print("\n-------- MENU --------")
        print("1. Create Table")
        print("2. Insert Value")
        print("3. Edit Value")
        print("4. View Table")
        print("5. Delete Row")
        print("6. Search Value")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            table()
        elif choice == "2":
            insert_value()
        elif choice == "3":
            edit()
        elif choice == "4":
            view()
        elif choice == "5":
            remove()
        elif choice == "6":
            search()
        elif choice == "7":
            print("Exiting... ")
            break
        else:
            print("Invalid choice")


menu()

