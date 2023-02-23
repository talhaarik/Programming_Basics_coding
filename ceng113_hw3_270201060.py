def main_menu():
    print("""1. Log in / change user
2. Create new user
3. Add friend
4. Show my friends
5. Exit""")


def isValid(myStr, what):  # Checks the password or username via datatype.
    if type(what) == list:  # Checks username
        Valid = True
        for i in range(len(myStr)):
            if myStr[i] not in valid_names:
                Valid = False
        for i in range(len(what)):
            if what[i][0] == myStr:
                Valid = False
        if (not Valid):
            print("Username not valid\n")
        return Valid

    if type(what) == type("a"):  # Checks the password
        Valid = False
        Length = False

        if len(myStr) <= 8 and len(myStr) >= 4:
            Length = True

        charCount = 0
        intCount = 0

        for j in range(len(myStr)):
            if myStr[j].isalpha():
                charCount += 1
            if myStr[j].isnumeric():
                intCount += 1
        if intCount > 0 and charCount > 0:
            Valid = True
        if not Valid or not Length:
            print("Password not valid\n")
        return Valid and Length


def friendList(myList):
    for j in range(len(myList)):
        if (user_name == myList[j][0]):
            print(myList[j][2])


with open("users.txt", "r+") as file:
    myList = [(line.strip()).split(";") for line in file]

option1 = False
valid_names = ["q", "w", "e", "r", "t", "y", "u", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "i", "z", "x",
               "c", "v", "b", "n", "m", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    main_menu()
    menu_operation = input("")
    option_list = ["1", "2", "3", "4", "5"]
    if (menu_operation not in option_list):
        print("Invalid option\n")
        continue
    if (menu_operation == '1'):
        option1 = True
        while True:
            user_name = input("Please enter username:\n")
            user_password = input("Please enter password:\n")
            for i in range(len(myList)):
                if (user_name == myList[i][0] and user_password == myList[i][1]):
                    option1 = True
                    print("Logged in\n")
                    break
            if (user_name != myList[i][0] or user_password != myList[i][1]):
                option1 = False
                print("Wrong password or username\n")
                break
            if option1:
                break
            if not option1:
                continue

    if (menu_operation == '2'):
        while True:
            new_user_name = input("Please enter username:\n")
            new_user_password = input("Please enter password:\n")

            if isValid(new_user_name, myList) and isValid(new_user_password, ""):
                addList = [new_user_name, new_user_password]
                addList.append("")
                myList.append(addList)
                break
            else:
                continue
        continue

    if (menu_operation == '3' and option1 == True):
        can_break = False
        control_in_list = False
        while True:
            new_friend = input("Please enter the name of your new friend:\n")
            for i in range(len(myList)):
                if (new_friend == myList[i][0]):
                    control_in_list = True
            if (control_in_list == False):
                print("Friend not found\n")
                break
            for i in range(len(myList)):
                if (myList[i][0] == user_name):
                    myList[i][-1] += "," + new_friend
                    can_break = True
            if (can_break == False):
                print("Friend not found\n")
                continue
            if (can_break):
                break


    if (menu_operation == '3' and option1 == False):
        print("You need to log in first\n")
        continue


    if (menu_operation == '4' and option1 == True):
        friendList(myList)


    if (menu_operation == '4' and option1 == False):
        print("You need to log in first\n")
        continue


    if (menu_operation == '5'):
        with open("users.txt", "w") as file:
            for i in range(len(myList)):
                file.write(myList[i][0] + ";" + myList[i][1] + ";" + myList[i][2] + "\n")
        break
