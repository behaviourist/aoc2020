with open("input.txt") as f:
  lines = f.readlines()

  valid = 0

  for i in lines:
    policy = {}

    policy["min"] = int(i.split(" ")[0].split("-")[0])
    policy["max"] = int(i.split(" ")[0].split("-")[1])
    policy["key"] = i.split(" ")[1].replace(":", "")
    policy["count"] = 0
  
    password = i.split(": ")[1].strip()

    for c in password:
      if c == policy["key"]:
        policy["count"] += 1

    if policy["count"] <= int(policy["max"]) and policy["count"] >= int(policy["min"]):
      valid += 1

  print(valid) # answer