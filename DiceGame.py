from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter your guess: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is %d" % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print "Your guess is above the maximum value."
  else:
    print "Rolling..."
    sleep(2)
    print "First roll is a %d" % first_roll
    sleep(1)
    print "And the second role is a %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total value is %d" % total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "Good job, you won"
    else:
      print "You lost, try again"

roll_dice(6)
