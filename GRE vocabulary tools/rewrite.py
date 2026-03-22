<<<<<<< HEAD


num = "25"
read_path = "Unit {}.html".format(num)
write_path = "Unit {}.txt".format(num)

with open(read_path, 'r', encoding="UTF-8") as f:
    c = f.readlines()
with open(write_path, 'w', encoding="UTF-8") as f:
    for j,i in enumerate(c):
        if j%4 in [0, 3]:
            f.write(i)
        elif j%4 == 1:
            f.write(c[j+1])
=======


num = "25"
read_path = "Unit {}.html".format(num)
write_path = "Unit {}.txt".format(num)

with open(read_path, 'r', encoding="UTF-8") as f:
    c = f.readlines()
with open(write_path, 'w', encoding="UTF-8") as f:
    for j,i in enumerate(c):
        if j%4 in [0, 3]:
            f.write(i)
        elif j%4 == 1:
            f.write(c[j+1])
>>>>>>> 2ceae69a4c81ebe4802c098fe21191cdd0ee2b42
            f.write(c[j])