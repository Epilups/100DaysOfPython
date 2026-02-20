import random

rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to a rock, paper and scissors game, please choose your move\nPress R for Rock, P for Paper, and S for Scissors")

#list of choices
choices = ['r', 'p', 's']

#user input
usermove = input()

#strings to display for user and computer in console ui
usersymbol = ''
computersymbol = ''

#what the value of the thing the user or computer chooses is
userchoice = ''

#for computer we just randomly generate its choice from the list using random.choice
computerchoice = random.choice(choices)

#assign computer symbol for ui based on what the randomizer selected
if computerchoice == 'r':
      computersymbol = rock
elif computerchoice == 'p':
      computersymbol = paper
else:
      computersymbol = scissors

#assign user data
if usermove == 'R':
      usersymbol = rock
      userchoice = choices[0]
elif usermove == 'P':
      usersymbol = paper
      userchoice = choices[1]
else:
      usersymbol = scissors
      userchoice = choices[2]


#logic for game

#make user and computer input into list
outcome = [userchoice, computerchoice]

#lists of conditions for user winning, computer winning, or a draw happening
userwins = [['r', 's'], ['p', 'r'], ['s', 'p']]
computerwins = [['r', 'p'], ['p', 's'], ['s', 'r']]
draw = [['r', 'r'], ['p', 'p'], ['s', 's']]

#print outcome
if outcome in userwins:
      print(f"You chose {userchoice}\n{usersymbol}\n The computer chose {computerchoice}\n{computersymbol}\n You win!")
elif outcome in computerwins:
      print(f"You chose {userchoice}\n{usersymbol}\n The computer chose {computerchoice}\n{computersymbol}\n You lose!")
else:
      print(f"You chose {userchoice}\n{usersymbol}\n The computer chose {computerchoice}\n{computersymbol}\n Its a draw!")







