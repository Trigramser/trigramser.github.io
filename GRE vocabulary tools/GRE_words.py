<<<<<<< HEAD
# 制作词汇表
# 形成只有单词的txt文档，一行一个单词，为后面制作词典做准备
read_path = "GRE vocabulary.html"
write_path = "GREwords.txt"

with open(read_path, 'r', encoding="UTF-8") as f:
    c = f.readlines()
with open(write_path, 'w', encoding="UTF-8") as f:
    for j,i in enumerate(c):
        if ":" in i and not "<summary>" in i and not "    " in i:
            if not '(' in i:
                f.write(i[:i.find(':')])
            else:
                f.write(i[:i.find('(')])
=======
# 制作词汇表
# 形成只有单词的txt文档，一行一个单词，为后面制作词典做准备
read_path = "GRE vocabulary.html"
write_path = "GREwords.txt"

with open(read_path, 'r', encoding="UTF-8") as f:
    c = f.readlines()
with open(write_path, 'w', encoding="UTF-8") as f:
    for j,i in enumerate(c):
        if ":" in i and not "<summary>" in i and not "    " in i:
            if not '(' in i:
                f.write(i[:i.find(':')])
            else:
                f.write(i[:i.find('(')])
>>>>>>> 2ceae69a4c81ebe4802c098fe21191cdd0ee2b42
            f.write('\n')