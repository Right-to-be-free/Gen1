name = input("what is your name? ")

print("Hello ", name) 

age = input("How old are you? ")

print("You are ", age, " years old")

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter your password: ")
    if password == "rockstar":
        print("Welcome to the system")
        break
    else:
        print("Access denied - wrong password")
        attempts += 1
        if attempts == max_attempts:
            print("Maximum attempts reached. Access denied.")
            reset = input("Do you want to reset your password? (yes/no): ")
            if reset == "yes":
                new_password = input("Enter your new password: ")
                print("Password reset successful. Please login with your new password.")
            else:
                print("Goodbye!")
                break
    
