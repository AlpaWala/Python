from datetime import date

volunteers = []
expenses = []
donations = []

# ==========================
# FILE HANDLING HELPERS
# ==========================

def save_all_volunteers():
    with open("volunteers.txt", "w") as file:
        for volunteer in volunteers:
            file.write(
                volunteer["name"] + "," +
                volunteer["city"] + "," +
                volunteer["skill"] + "\n"
            )

def load_volunteers():
    try:
        with open("volunteers.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    volunteers.append({
                        "name": parts[0],
                        "city": parts[1],
                        "skill": parts[2]
                    })
    except FileNotFoundError:
        pass

def save_all_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(
                expense["category"] + "," +
                str(expense["amount"]) + "\n"
            )

def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    expenses.append({
                        "category": parts[0],
                        "amount": float(parts[1])
                    })
    except FileNotFoundError:
        pass

def save_all_donations():
    with open("donations.txt", "w") as file:
        for donation in donations:
            file.write(
                donation["donor_name"] + "," +
                str(donation["amount"]) + "," +
                donation["date"] + "\n"
            )

def load_donations():
    try:
        with open("donations.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    donations.append({
                        "donor_name": parts[0],
                        "amount": float(parts[1]),
                        "date": parts[2]
                    })
    except FileNotFoundError:
        pass

# ==========================
# VOLUNTEERS
# ==========================

def add_volunteer():
    volunteer = {
        "name": input("Enter Name: "),
        "city": input("Enter City: "),
        "skill": input("Enter Skill: ")
    }
    volunteers.append(volunteer)
    save_all_volunteers()
    print("Volunteer Added!")

def view_volunteers():
    if not volunteers:
        print("No Volunteers Found")
        return
    for volunteer in volunteers:
        print(volunteer)

def search_volunteer():
    name = input("Enter Name: ")
    for volunteer in volunteers:
        if volunteer["name"] == name:
            print(volunteer)
            return
    print("Volunteer Not Found")

def delete_volunteer():
    name = input("Enter Name To Delete: ")
    for volunteer in volunteers:
        if volunteer["name"] == name:
            volunteers.remove(volunteer)
            save_all_volunteers()
            print("Volunteer Deleted")
            return
    print("Volunteer Not Found")

# ==========================
# EXPENSES
# ==========================

def add_expense():
    expense = {
        "category": input("Enter Category: "),
        "amount": float(input("Enter Amount: "))
    }
    expenses.append(expense)
    save_all_expenses()
    print("Expense Added!")

def view_expenses():
    if not expenses:
        print("No Expenses Found")
        return
    for expense in expenses:
        print(expense)

def search_expense():
    category = input("Enter Category: ")
    for expense in expenses:
        if expense["category"] == category:
            print(expense)
            return
    print("Expense Not Found")

def delete_expense():
    category = input("Enter Category To Delete: ")
    amount = float(input("Enter Amount To Delete: "))
    for expense in expenses:
        if expense["category"] == category and expense["amount"] == amount:
            expenses.remove(expense)
            save_all_expenses()
            print("Expense Deleted")
            return
    print("Expense Not Found")

def total_spending():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print("Total Spending:", total)

# ==========================
# DONATIONS
# ==========================

def add_donation():
    donation = {
        "donor_name": input("Enter Donor Name: "),
        "amount": float(input("Enter Amount: ")),
        "date": str(date.today())
    }
    donations.append(donation)
    save_all_donations()
    print("Donation Added!")

def view_donations():
    if not donations:
        print("No Donations Found")
        return
    for donation in donations:
        print(donation)

def search_donor():
    name = input("Enter Donor Name: ")
    for donation in donations:
        if donation["donor_name"] == name:
            print(donation)
            return
    print("Donor Not Found")

def delete_donation():
    name = input("Enter Donor Name To Delete: ")
    amount = float(input("Enter Donation Amount To Delete: "))
    for donation in donations:
        if donation["donor_name"] == name and donation["amount"] == amount:
            donations.remove(donation)
            save_all_donations()
            print("Donation Deleted")
            return
    print("Donation Not Found")

def total_donations():
    total = 0
    for donation in donations:
        total += donation["amount"]
    print("Total Donations:", total)

# ==========================
# REPORT
# ==========================

def generate_report():
    total_donation_amount = sum(d["amount"] for d in donations)
    total_expense_amount = sum(e["amount"] for e in expenses)
    balance = total_donation_amount - total_expense_amount

    print("\n===== NGO REPORT =====")
    print("Total Volunteers:", len(volunteers))
    print("Total Donations:", total_donation_amount)
    print("Total Expenses:", total_expense_amount)
    print("Remaining Balance:", balance)

# ==========================
# MENUS
# ==========================

def volunteer_menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Delete 5.Back")
        c = input("Choice: ")
        if c == "1": add_volunteer()
        elif c == "2": view_volunteers()
        elif c == "3": search_volunteer()
        elif c == "4": delete_volunteer()
        elif c == "5": break

def expense_menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Delete 5.Total 6.Back")
        c = input("Choice: ")
        if c == "1": add_expense()
        elif c == "2": view_expenses()
        elif c == "3": search_expense()
        elif c == "4": delete_expense()
        elif c == "5": total_spending()
        elif c == "6": break

def donation_menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Delete 5.Total 6.Back")
        c = input("Choice: ")
        if c == "1": add_donation()
        elif c == "2": view_donations()
        elif c == "3": search_donor()
        elif c == "4": delete_donation()
        elif c == "5": total_donations()
        elif c == "6": break

load_volunteers()
load_expenses()
load_donations()

while True:
    print("\n===== NGO MANAGEMENT SYSTEM V3 =====")
    print("1. Volunteer Management")
    print("2. Expense Management")
    print("3. Donation Management")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        volunteer_menu()
    elif choice == "2":
        expense_menu()
    elif choice == "3":
        donation_menu()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
