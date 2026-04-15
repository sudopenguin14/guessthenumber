import random
def game():
  num= random.randint(1,100)
  guess=0
  print("I'm thinking of a number between 1 and 100. Can you guess it?")
  while guess != num:
    try:
      guess=int(input("Enter your guess:"))
      if guess<num:
        print("Too low! Try again")
      elif guess>num:
        print("Too high! Try again")
      else:
        print("Correct! The number was",num,"." "You've won the game")
    except ValueError:
      print("Please enter a valid whole number")
game()
    
  