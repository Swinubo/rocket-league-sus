import easygui

Name = easygui.enterbox("What is your account name?")

with open("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Accounts.txt", "a") as Accounts:
    Accounts.write("\n" + Name)
    Accounts.close()