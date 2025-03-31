import random

#global variable which is accessible throughtout anywhere

global_variable_roll_count=3

#function for rolling dice


#local variables are die_1 and die_2 which is only accessible within function roll_dice

def roll_dice():
  die_1 = random.randint(1,6)
  die_2 = random.randint(1,6)
  return die_1,die_2

#main function to call roll_dice function

def main_dice_roll():
  for i in range(global_variable_roll_count):
    die_1,die_2=roll_dice()
    print(f'Roll # {i+1}= Die 1: "{die_1}" Die 2: "{die_2}"')

main_dice_roll()