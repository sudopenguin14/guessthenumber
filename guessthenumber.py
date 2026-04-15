import random
def game():
  num= random.randint(1,100)
  attempts=5
  guess=0
  print("I'm thinking of a number between 1 and 100")
  print("You have 5 attempts. Can you guess it?")
  while guess != num and attempts>0:
    try:
      print(f"\nAttempts remaining {attempts}")
      guess=int(input("Enter your guess:"))
      attempts -=1
      if guess<num:
        print("Too low! Try again")
      elif guess>num:
        print("Too high! Try again")
      else:
        print("Correct! The number was",num,"." "You've won the game")
        return True
    except ValueError:
      print("Please enter a valid whole number")
  print("\nGame Over!")
  print("You have run out of attempts. You lost. The number was ",num)
  return False
while True:
  game()
  retry=input("\nDo you want to play again?[y/n]").lower().strip()
  if retry!='y':
    print("Thanks for playing. Goodbye")
    break
input(f"\nPress Enter to exit...")