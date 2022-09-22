#HighLow.py
#Ryan Carroll
#CTS 115 (NL01)
# High Low Game

correct_number = 7
user_number = int(input("Guess a number between 0-9:\t "))
if user_number == correct_number:
    print(f"Your guess is: {user_number}, You win!")
else:
    print(f"WRONG! Correct number is {correct_number}")

print("Program End")