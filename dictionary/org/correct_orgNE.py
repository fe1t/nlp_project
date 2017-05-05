filename = "orgNE_add.txt"

with open(filename, "r") as f:
    data = map(lambda x: x.replace("|", "").rstrip("\n"), f.readlines())

for _data in data:
    print _data
