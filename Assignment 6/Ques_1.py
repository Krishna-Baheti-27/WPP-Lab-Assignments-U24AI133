class PasswordManager:
    def __init__(self):
        self.old_passwords = []
    
    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None
    
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False
    
    def is_correct(self, password):
        return password == self.get_password()

# Dynamic user input
pm = PasswordManager()
while True:
    print("\n1. Set Password\n2. Get Current Password\n3. Check Password\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        new_password = input("Enter new password: ")
        if pm.set_password(new_password):
            print("Password set successfully.")
        else:
            print("Password already used. Choose a different one.")
    elif choice == "2":
        print("Current Password:", pm.get_password())
    elif choice == "3":
        check_password = input("Enter password to check: ")
        if pm.is_correct(check_password):
            print("Password is correct.")
        else:
            print("Incorrect password.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
