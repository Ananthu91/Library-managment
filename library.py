import getpass

memberships = {}
session = {'role': None}

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Membership")
        print("2. Update Membership")
        print("3. View All Memberships")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_membership()
        elif choice == '2':
            update_membership()
        elif choice == '3':
            view_memberships()
        elif choice == '4':
            print("Logging out...")
            session['role'] = None
            break
        else:
            print("Invalid choice. Try again.")

def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. View Memberships")
        print("2. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_memberships()
        elif choice == '2':
            print("Logging out...")
            session['role'] = None
            break
        else:
            print("Invalid choice. Try again.")

def add_membership():
    print("\n--- Add Membership ---")
    member_id = input("Enter Membership ID: ").strip()

    if not member_id:
        print("Membership ID is mandatory.")
        return

    if member_id in memberships:
        print("Membership ID already exists.")

    name = input("Enter Member Name: ").strip()
    if not name:
        print("Member Name is mandatory.")
        return

    duration = input("Select Duration (6 months / 1 year / 2 years): ").strip()

    if duration not in ['6 months', '1 year', '2 years']:
        print("Invalid duration. Defaulting to 6 months.")
        duration = '6 months'

    memberships[member_id] = {'name': name, 'duration': duration}
    print(f"Membership added successfully for {name} with duration {duration}.")

def update_membership():
    print("\n--- Update Membership ---")
    member_id = input("Enter Membership ID: ").strip()

    if not member_id:
        print("Membership ID is mandatory.")
        return

    if member_id not in memberships:
        print("Membership ID not found.")
        return

    print("1. Extend Membership")
    print("2. Cancel Membership")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        memberships[member_id]['duration'] = '6 months'
        print("Membership extended by 6 months.")
    elif choice == '2':
        del memberships[member_id]
        print("Membership cancelled.")
    else:
         print("Invalid choice.")

def view_memberships():
    print("\n--- View Memberships ---")
    if not memberships:
        print("No memberships available.")
    else:
        for member_id, details in memberships.items():
            print(f"ID: {member_id}, Name: {details['name']}, Duration: {details['duration']}")

def login():
    print("\n--- Library Management System ---")
    print("Login as Admin or User")
    while True:
        username = input("Enter username (admin/user): ").strip().lower()
        password = getpass.getpass("Enter password: ").strip()

        if username == 'admin' and password == 'admin123':
            session['role'] = 'admin'
            print("Admin login successful.")
            admin_menu()
            break
        elif username == 'user' and password == 'user123':
            session['role'] = 'user'
            print("User login successful.")
            user_menu()
            break
        else:
            print("Invalid credentials. Try again.")

def main():
    while True:
        login()
        if session['role'] is None:
             break

if __name__ == "__main__":
    main()
