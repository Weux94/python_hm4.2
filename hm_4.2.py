LIST = [6, 5, 12, 5]
value = 0
for item in LIST:
    if (LIST.index(item) % 2 == 0):
        value = value + item

print(value * LIST[len(LIST) - 1])
