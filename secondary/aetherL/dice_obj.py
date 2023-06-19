import random

# Pick the dice that u want

dice_number = int(input("Enter dice number..."))
random_number = 0
random_num_2 = 0
random_num_3 = 0
random_num_4 = 0
real = 0

# Roll the dice

if dice_number == 4:
  random_number = random.randint(1,4)
  print("You rolled a",random_number)


if dice_number == 6:
  random_num2 = random.randint(1,6)
  print("You rolled a", random_num_2)


if dice_number == 12:
  random_num3 = random.randint(1,12)
  print("You rolled a",random_num3)

if dice_number == 24:
  random_num4 = random.randint(1,24)
  print("You rolled a",random_num4)

# Add the dice together and multiply by a random number

total_random = random.randint(1,1100000000000000000000)

if dice_number == 4:
  real = total_random * random_number

if dice_number == 6:
  real = total_random * random_num2

if dice_number == 12:
  real = total_random * random_num3

if dice_number == 24:
  real = total_random * random_num4

print ("Your randomised number:",real)