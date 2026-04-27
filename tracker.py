from storage import load, save
from datetime import datetime

def add_expense():
    try:
        amount = int(input("Enter amount: ").strip())
        Type = input("Enter type: ").lower().strip()
        if Type != '':
            category = input("Enter category: ").lower().strip()
            if category != "":
                note = input("Enter a note: ").lower().strip()
                if note!= "":
                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    data = load()
                    data[time] = {
                        "Type": Type,
                        "Amount": amount,
                        "Category": category,
                        "Note": note
                    }

                    save(data)
                    print("<<_Expense added->>")
    
                else:
                    print("note cannot be empty!")
                    return        
            else:
                print("Category cannot be empty!")
                return
        else:
            print("Type cannot be empty!")
            return
    except ValueError:
        print("Invalid input! Enter numbers.")
        return
                

def show_expenses():
    data = load()

    for time, details in data.items():
        print(f"\nTime : {time}")
        print(f"Amount : {details['Amount']}")
        print(f"Type : {details['Type']}")
        if details['Type'] != 'income':
            print(f"Category : {details['Category']}")
            print(f"Note : {details['Note']}")
        print("\n")


def add_income():
    try:
        income = int(input("Enter your income: ").strip())
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = load()
        data[time] = {
            "Type": "income",
            "Amount": income
        }

        save(data)
        print("<<-Income saved->>")
        
    except ValueError:
        print("Invalid input! Enter numbers only.")


    




