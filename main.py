from tracker import add_entry
from tracker import show_all
from tracker import check_balance
from tracker import del_expense
from tracker import update_entry
from tracker import show_expenses
from tracker import show_incomes
from tracker import show_total_income
from tracker import show_total_expenses
from tracker import monthly_balance
from tracker import monthly_summary
from tracker import category_breakdown
from tracker import show_by_date

def main():
    print("<<--Finance Tracker-->>" + "\n")

    while True:
        
        print("1. Add an entry")
        print("2. Show all expenses")
        print("3. Check balance")
        print("4. Delete an entry")
        print("5. Update an entry")
        print("6. Show expenses")
        print("7. Show incomes")
        print("8. show monthly summary")
        print("9. show category wise sumamry")
        print("10. Search an entry by date")
        print("11. Exit")

        user = input("Enter choice: ").strip()

        if user != "":           
            if user == "1":
                add_entry()
                print("\n")
            elif user == "2":
                show_all()
                print("\n")
            elif user == "3":
                check_balance()
                print("\n")
            elif user == "4":
                print("\n")
                del_expense()
                print("\n")
            elif user == "5":
                print("\n")
                update_entry()
                print("\n")
            elif user == "6":
                print("\n")
                show_expenses()
                print("\n")
            elif user == "7":
                print("\n")
                show_incomes()
                print("\n")
            elif user == "8":
                monthly_summary()
                print("\n")   
            elif user == "9":
                print("\n")
                category_breakdown()
                print("\n") 
            elif user == "10":
                print("\n") 
                show_by_date()
                print("\n")  
            elif user == "11":
                print("Goodbye!\n")
                break
            else:
                print("Invalid choice! Enter 1 to 11\n")
        else:
            print("Choice cannot be empty!\n")


main()







