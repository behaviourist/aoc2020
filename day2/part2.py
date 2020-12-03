with open("input.txt") as f:
  lines = f.readlines()

  valid = 0

  for i in lines:
    index = [int(i.split(" ")[0].split("-")[0])-1, int(i.split(" ")[0].split("-")[1])-1]
    password = i.split(": ")[1]
    key = i.split(" ")[1].replace(":", "")

    if password[index[0]] == key and password[index[1]] == key:
      continue

    if password[index[0]] == key or password[index[1]] == key:
      valid += 1

  print(valid) # answer