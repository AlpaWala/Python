# NGO Volunteer Management System

volunteers = []


def add_volunteer():

    name = input("Enter Volunteer Name: ")
    city = input("Enter Volunteer City: ")
    skill = input("Enter Volunteer Skill: ")

    volunteer = {
        "name": name,
        "city": city,
        "skill": skill
    }

    volunteers.append(volunteer)

    print("Volunteer Added Successfully!")


def view_volunteers():

    if len(volunteers) == 0:
        print("No Volunteers Found")

    else:

        print("\nVolunteer List")

        for volunteer in volunteers:

            print("---------------------")
            print("Name :", volunteer["name"])
            print("City :", volunteer["city"])
            print("Skill :", volunteer["skill"])


def search_volunteer():

    search_name = input("Enter Volunteer Name To Search: ")

    found = False

    for volunteer in volunteers:

        if volunteer["name"] == search_name:

            print("\nVolunteer Found")
            print("Name :", volunteer["name"])
            print("City :", volunteer["city"])
            print("Skill :", volunteer["skill"])

            found = True
            break

    if found == False:
        print("Volunteer Not Found")


def delete_volunteer():

    delete_name = input("Enter Volunteer Name To Delete: ")

    found = False

    for volunteer in volunteers:

        if volunteer["name"] == delete_name:

            volunteers.remove(volunteer)

            print("Volunteer Deleted Successfully")

            found = True
            break

    if found == False:
        print("Volunteer Not Found")


while True:

    print("\n===== NGO Volunteer Management System =====")
    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Search Volunteer")
    print("4. Delete Volunteer")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_volunteer()

    elif choice == "2":
        view_volunteers()

    elif choice == "3":
        search_volunteer()

    elif choice == "4":
        delete_volunteer()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")