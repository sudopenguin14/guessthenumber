import random
def game():
  print("I have chosen a number between 1 and 100.")
  print("You have a total of 5 attempts. Can you guess it?")
  num=random.randint(1,100)
  guess=0 
  attempt=5
  while guess!=num and attempt>0:
    try:
      print("\nYou have ",attempt,"attempts remaining")
      guess=int(input("Enter your guess:"))
      attempt-=1
      if guess<num:
        print("Too low! Try again")
      elif guess>num:
        print("Too high! Try again")
      else:
        print("You have won! The number was ",num)
        return True
    except ValueError:
      print("\nPlease enter a valid whole number")
  print("\nGame Over!")
  print("You Lost! The number was ",num)
  return False
while True:
  game()
  retry=input("\nDo you want to try again?[y/n]:").lower().strip()
  if retry!='y':
    print("\nThank You for playing. Goodbye")
    break
input(f"\nPress ENTER to exit")

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
