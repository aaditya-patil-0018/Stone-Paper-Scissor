import random
options = ['Stone', 'Paper', 'Scissor']

# Asking user name
userName = str(input('Your Name: '))

# Rules of Game....
def rules():
    print('''
1 for Stone,
2 for Paper,
3 for Scissor
To Quit press -- Q
For Help Press -- H
    ''')

rounds = int(input('How many rounds you want to play: '))
rules()

userPoints = 0}
computerPoints = 0

for i in range(rounds):
    computerSelectedOption =random.choice(options)
    userOption = input('> ')
    print(f'> {computerSelectedOption}')
    if userOption == '1' and computerSelectedOption == 'Paper' or userOption == '2' and computerSelectedOption == 'Scissor' or userOption == '3' and computerSelectedOption == 'Stone':
        computerPoints += 1
        print(f'''
Points:
{userName} = {userPoints}
Computer = {computerPoints}
''')
    elif userOption == '1' and computerSelectedOption == 'Scissor' or userOption == '2' and computerSelectedOption == 'Stone' or userOption == '3' and computerSelectedOption == 'Paper':
        userPoints += 1
        print(f'''
Points:
{userName} = {userPoints}
Computer = {computerPoints}
''')
    elif userOption == 'H' or userOption == 'h':
        rules()
        rounds += 1
    elif userOption == 'R' or userOption == 'r':
        rounds = rounds + i
        print('Match is Restarted !')
    elif userOption == 'Q' or userOption == 'q':
        break
    else:
        print(f'''
Points:
{userName} = {userPoints}
Computer = {computerPoints}
''')

if userPoints > computerPoints:
    print(f'{userName} Won !!')
elif userPoints < computerPoints:
    print('Computer Won ! Try Again.')
else:
    print('Match is Draw.')
