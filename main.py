import random
import sys

rock_pic = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_pic = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_pic = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Let's play Rock, Paper, Scissors!\nType 0 for Rock, 1 for Paper or 2 for Scissors:\n")

list_user = ["0", "1", "2"]

if int(user_choice) >= 3:
  print("You typed an invalid number! You lose!")
  sys.exit()
elif user_choice == "0":
  print("\n\n" + rock_pic)
elif user_choice == "1":
  print("\n\n" + paper_pic)
else:
  print("\n\n" + scissors_pic)
  

computer_choice = str(random.randint(0,2))

list_computer = ["0", "1", "2"]

if computer_choice == "0":
  print("\n\nComputer chose:\n\n" + rock_pic)
elif computer_choice == "1":
  print("\n\nComputer chose:\n\n" + paper_pic)
else:
  print("\n\nComputer chose:\n\n" + scissors_pic)


winning_1 = str(list_user[0]) + str(list_computer[2])
winning_2 = str(list_user[1]) + str(list_computer[0])
winning_3 = str(list_user[2]) + str(list_computer[1])

if user_choice == computer_choice:
  print("\nIt's a draw!")
elif str((list_user[int(user_choice)]) + str(list_computer[int(computer_choice)])) == winning_1:
  print("\nYou win!")
elif str((list_user[int(user_choice)]) + str(list_computer[int(computer_choice)])) == winning_2:
  print("\nYou win!")
elif str((list_user[int(user_choice)]) + str(list_computer[int(computer_choice)])) == winning_3:
  print("\nYou win!")
else:
  print("\nYou lose! Haha!")




