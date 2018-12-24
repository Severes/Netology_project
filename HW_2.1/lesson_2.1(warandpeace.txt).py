count = 0

with open("warandpeace.txt") as text:
    for line in text:
        if "Пьер" in line and "Наташ" in line:
            count += 1

print("Пьер и Наташа встретились на "\
      "{} строках".format(count))

