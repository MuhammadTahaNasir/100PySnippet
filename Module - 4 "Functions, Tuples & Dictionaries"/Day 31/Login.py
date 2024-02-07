def login_system():
    #The example login is setted as follow
    correct_username = "user1122"
    correct_password = "password123"                                                            

    # Asking the user to input username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username and password match the correct credentials
    if username == correct_username and password == correct_password:
        print("Login successful! Welcome, " + username + "!")
    else:
        print("Incorrect username or password. Please try again.")

if __name__ == "__main__":
    login_system()
   
