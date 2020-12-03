with open("input.txt") as f:
  lines = f.readlines()

  for x in lines:
    x = int(x)
    for y in lines:
      y = int(y)
      for z in lines:
        z = int(z)

        if x + y + z == 2020:
          print(x * y * z) # answer
          exit()