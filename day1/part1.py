with open("input.txt") as f:
  lines = f.readlines()

  for x in lines:
    x = int(x)
    for y in lines:
      y = int(y)

      if x + y == 2020:
        print(x * y) # answer
        exit()