f = open("months.txt")
next = f.readline()
items = []
while next != "":
    print(next)
    items.append(len(next))
    next = f.readline()

print items