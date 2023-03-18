Player = (input('What is your account name? \n'))

Accounts = open('C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Accounts.txt', 'r')
AccountsR = Accounts.readlines()
AccountList = []
LevelList = []

CurrentLine = -1
for line in AccountsR:
    CurrentLine += 1
    Name = line[2:]
    Name = Name.strip()
    Level = line[:1]
    AccountList.append(Name.strip())
    LevelList.append(Level.strip())
    if Name == Player:
        print('We have found your name!')
        print('You are on level ' + Level + ' and your name is ' + Name + '.')
