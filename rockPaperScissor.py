import random

option_list = ["ROCK","PAPER","SCISSOR"]
user = input("ENTER YOUR CHOICE IN CAPITAL LETTERS: ROCK :PAPER :SCISSOR:::")
user_choice = user.upper()
computer_choice = random.choice(option_list)

print("USER CHOICE --" + user_choice)
print("COMPUTER CHOICE --" + computer_choice)

if user_choice==computer_choice:
    print("Oppss..Its a Tie..!")
    print("Try Again")
elif user_choice=="ROCK":
    if computer_choice=="SCISSOR":
       print("YOU WIN :)")
    else:
       print("COMPUTER WIN :(")
elif user_choice == "PAPER":
    if computer_choice=="ROCK":
       print("YOU WIN :)")
    else:
       print("COMPUTER WIN :(")
else:
    if computer_choice=="PAPER":
       print("YOU WIN :)")
    else:
       print("COMPUTER WIN :(")
    