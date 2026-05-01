from storage import load, save
from datetime import datetime


def print_entry(time, details):
    print(f"\nTime: {time}")
    print(f"Type: {details['Type']}")
    print(f"Amount: {details['Amount']}")
    if details['Type'] != "income":
        print(f"Category: {details['Category']}")
        print(f"Note: {details['Note']}")
    if details['Type'] == "income":
        print(f"Note: {details['Note']}")
    print("\n")


def get_entry(prompt="Enter time: "):
    data = load()
    time = input(prompt).strip()
    if not time:
        print("Time cannot be empty!")
        return None, None 
    if time not in data:
        print("Time does not exist")
        return None, None
    return time, data


def add_entry():

    data = load()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:")
    Type = input("Enter type: ").lower().strip()
    if Type in ["income", "expense"]:
        if Type == "income": 
            try:
                amount = int(input("Enter amount: ").strip())
                note = input("Enter a note: ").strip()
                if note != "":
                    data[time] = {
                        "Time": time,
                        "Type": Type,
                        "Amount": amount,
                        "Note": note
                    }
                    save(data)
                    print("<-Income Saved->\n")
                    return
                else:
                    print("Note can't be empty!")
                    return                
            except ValueError:
                print("Enter numbers only!")

        if Type == "expense":
            try:
                amount = int(input("Enter amount: ").strip())
                category = input("Enter category: ").lower().strip()
                if category in ["food", "shopping", "transport", "bills", "other"]:
                    if category != "":
                        note = input("Enter a note: ").strip()
                        if note != "":
                            data[time] = {
                                "Time": time,
                                "Type": "expense",
                                "Category": category, 
                                "Amount": amount,
                                "Note": note
                            }            
                            save(data)
                            print("<-Expense Saved->\n")
                        else:
                            print("Note cab't be empty!")
                    else:
                        print("Category can't be empty!")
                else:
                    print("Category should be food, shopping, transport, bills or other. ")
            except ValueError:
                print("Enter numbers only!")        
    else:
        print("Type should be either income or expense.")
        return
            
    
def show_all():
    data = load()

    for time, details in data.items():
        print_entry(time, details)


        
def check_balance():
    data = load()
    income = 0 
    expenses = 0 
    for time, details in data.items():
        if details['Type'] == 'income':
            income += details['Amount']
        else:
            expenses += details['Amount']
            
    balance = income - expenses
    print(f"Current Balance: {balance}" + "\n")


def del_expense():
    data = load()
    for time, details in data.items():
        print_entry(time, details)
        
    time, data = get_entry()
    if time is None:
        return

    confirm = input("Do you want to continue? (y/n) ").lower().strip()
    if confirm != "n":
        del data[time]
        save(data)
        print("<-Entry Deleted->")


def update_entry():
    data = load()
    for time, details in data.items():
        print_entry(time, details)
        
    time, data = get_entry()
    if time is None:
        return
        
    try:
        amount = int(input("Enter amount: ").strip())
        Type = input("Enter type: ").lower().strip()
        if Type != "":
            if Type == "income":
                data[time] = {
                    "Amount": amount,
                    "Type": "income"
                }
                save(data)
                print("<-Entry Updated->\n")
            if Type != 'income':
                category = input("Enter category: ").lower().strip()
                if category != "":
                    note = input("Enter note: ").lower().strip()
                    if note != "":
                        data[time] = {
                            "Type": Type,
                            "Amount": amount,
                            "Category": category,
                            "Note": note
                        }
                        save(data)
                        print("<-Entry Updated->")
                    else:
                        print("Note cannot be empty!")
                        return
                else:
                    print("Category cannot be empty!")
        else:
            print("Type cannot be empty!")
            return
    except ValueError:
        print("Enter numbers only.")

  
def show_incomes():
    data = load()
    for time, details in data.items():
        if details['Type'] == 'income':
            print(f"Time: {time}")
            print(f"Type: income")
            print(f"Amount: {details['Amount']}")
            print(f"Note: {details['Note']}")
        print("\n")


def show_expenses():
    data = load()
    for time, details in data.items():
        if details['Type'] == 'expense':
            print(f"Time: {time}")
            print(f"Type: expense")
            print(f"Amount: {details['Amount']}")
            print(f"Category: {details['Category']}")
            print(f"Note: {details['Note']}")
        print("\n")
                    
def get_month():
    data = load()
    month = input("Enter month (01-12) ").strip()
    if month != "":
        return month
    else:
        print("Month can't be empty!")
        return None
 
        
def show_total_income(month):
    data = load()
    count_income = 0
    total_income = 0 
    for time, details in data.items():
        if time[5:7] == month:
            if details['Type'] == "income":
                count_income += 1
                total_income += details["Amount"]

    return count_income, total_income


def show_total_expenses(month):
    data = load()
    count_expenses = 0            
    total_expense = 0            
    for time, details in data.items():
        if time[5:7] == month:
            if details['Type'] == "expense":
                count_expenses += 1
                total_expense += details['Amount']

    return count_expenses, total_expense

def monthly_balance(total_expense, total_income):
        balance = total_income - total_expense
        return balance

def monthly_summary():

    month = get_month()
    if month is None:
        return

    count_income, total_income = show_total_income(month)
    count_expenses, total_expense = show_total_expenses(month)
    balance = monthly_balance(total_expense, total_income)

         
    print(f"\nTotal number of Incomes: {count_income}\n")
    print(f"Total Income: {total_income}\n")
    print(f"Total number of Expenses: {count_expenses}\n")
    print(f"Total Expense: {total_expense}\n")
    print(f"Month's balance: {balance}\n")



monthly_summary()
