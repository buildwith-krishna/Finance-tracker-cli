from tracker import add_expense
from tracker import show_expenses
from tracker import add_income
from tracker import check_balance

def main():
    print("<<--Finance Tracker-->>" + "\n")

    while True:
        
        print("1. Add income")
        print("2. Add expense")
        print("3. Show all expenses")
        print("4. Check balance")
        print("5. Exit")

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
                check_balance()
                print("\n")
            elif user == "5":
                print("Goodbye!\n")
                break
            else:
                print("Invalid choice! Enter 1 to 5\n")
        else:
            print("Choice cannot be empty!\n")

main()







