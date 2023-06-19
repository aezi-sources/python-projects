letter_a = int(input("Enter A: "))
letter_b = int(input("Enter B: "))

while letter_b != 0:
  if letter_a > letter_b:
    letter_a = letter_a - letter_b;
  else:
    letter_b = letter_b - letter_a;
print(letter_a)