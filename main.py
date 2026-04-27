from tracker import add_expense
from tracker import show_expenses
from tracker import add_income

def main():
    print("<<--Finance Tracker-->>" + "\n")

    while True:
        
        print("1. Add income")
        print("2. Add expense")
        print("3. Show all expenses")
        print("4. Exit")

        user = input("Enter choice: ").strip()

        if user != "":
            if user == "1":
                add_income()
                print("\n")           
            elif user == "2":
                add_expense()
                print("\n")
            elif user == "3":
                show_expenses()
                print("\n")
            elif user == "4":
                print("Goodbye!\n")
                break
            else:
                print("Invalid choice! Enter 1 to 4")
        else:
            print("Choice cannot be empty!\n")

main()







