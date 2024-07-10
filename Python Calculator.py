import math

while True:
  equation_to_solve = input("Input your equation: ")
  a = [*equation_to_solve]
  length_a = len(a)
  solve = ""
  
  for i in range(length_a):
    if a[i] == "x":
      a[i] = "*"
    elif a[i] == "^":
      a[i] = "**"
  print(eval(solve.join(a)))