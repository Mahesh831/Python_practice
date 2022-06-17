#same program but in other way
name = input('Enter name')
count = 0
for i in name:
    if i.isdigit():
        count = count + 1
print(count)
        