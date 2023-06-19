from random import *

wages = (random() + 1) * 100
earn = 50
limit = 200

wages_earned = wages + earn

if wages_earned > limit:
  print("you are paying too much")
  print(wages_earned)

if wages_earned < limit:
  print("good enough")
  print(wages_earned)