username = input("Enter Username: ")
password = input("Enter Password: ")

hidden_password = len(password) * '*'
print(f"{username}, you password {hidden_password} is {len(password)} letters long")