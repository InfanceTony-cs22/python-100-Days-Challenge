def user_name(username):
    if len(username)<=3:
        print("Invalid user name Must be atleast contain 4 characters long.")
    elif len(username)>15:
            print("Invalid username. Must be less than 15 characters")
    else:
            print("valid username !.")
