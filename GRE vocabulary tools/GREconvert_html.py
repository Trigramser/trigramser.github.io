<<<<<<< HEAD
import re
import os

# read_path = "GRE vocabulary.txt"
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if u"\u4e00" <= uchar <= u"\u9fff":
        return True
    else:
        return False

name = "Unit 30"

read_path = "b {}.txt".format(name)
rewrite_path = "{}.txt".format(name)
write_path = "unit GRE vocabulary.html"

# # # # 1、
# my_re = re.compile(r'[A-Za-z]',re.S)
# with open(read_path, 'r', encoding="UTF-8") as f:
#     c = f.readlines()
# with open(rewrite_path, 'w', encoding="UTF-8") as f:
#     for i in c:
#         res_n = re.findall(my_re, i.rstrip('\n'))
#         decerator = False
#         for j in i:
#             if is_chinese(j[0]):
#                 decerator = '#'
#                 i = i.replace(' ', '').replace(',', '，').replace('.', '。').replace('(', '（').replace(')', '）'.replace(':', '：'))
#                 f.write('#'+i)
#                 break
#         if ' ' in i[:-2]:
#             i = i.replace(',', ', ').replace('  ', ' ')
#             f.write('    '+i)
#         elif res_n:
#             f.write(i.rstrip('\n').rstrip()+":\n")
#         elif i == '\n':
#             f.write(i)


# # # # 2、 version 1.0
# with open(rewrite_path, 'r', encoding="UTF-8") as f:
#     c = f.readlines()

# with open(write_path, 'w', encoding="UTF-8") as f:
#     c_len = 0
#     for i in c:
#         if i.endswith(":\n"):
#             c_len+=1
#     print(c_len)
#     num = 0
#     test_2 = True
#     for j,i in enumerate(c):
#         if i.endswith(":\n"):
#             num+=1
#         if num%10 == 1 and test_2:
#             if num//10 < c_len//10:
#                 f.write("<h5>{} - {}</h5>\n".format(num, num+9))
#             else:
#                 f.write("<h5>{} - {}</h5>\n".format(num, c_len))
#             test_2 = False
#         if num%10 == 2:
#             test_2 = True

#         if i.startswith("    "):
#             f.write("<a href=\"javascript:void(null);\" title=\"{}\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>{}</br>\n".format(c[j+1][1:-1], i.strip()))
#         elif i[0] != '#':
#             f.write(i.replace('\n', "</br>\n"))

# # # 2、 version 2.0
def version_2_GRE(rewrite_path, write_path):
    with open(rewrite_path, 'r', encoding="UTF-8") as f:
        c = f.readlines()

    with open(write_path, 'w', encoding="UTF-8") as f:
        c_len = 0
        for i in c:
            if i.endswith("]\n"):
                c_len+=1
        print(c_len)
        num = 0
        test_2 = True
        for j,i in enumerate(c):
            if i.endswith("]\n"):
                num+=1
            if num%10 == 1 and test_2:
                if num//10 < c_len//10:
                    f.write("<h5>{} - {}</h5>\n".format(num, num+9))
                else:
                    f.write("<h5>{} - {}</h5>\n".format(num, c_len))
                test_2 = False
            if num%10 == 2:
                test_2 = True

            if i.endswith("]\n"):
                f.write("<details><summary class=\"vocabulary\">\n")
                f.write("{} <span class=\"phonetic\">{}</span></summary>\n".format(i[:i.find(':')], i[i.find(':'):].rstrip('\n')))
            elif i.startswith("$"):
                f.write("<div class=\"word\">{}</div>".format(i.strip('$').rstrip('\n')))
                f.write("\n")
            elif i.startswith("%"):
                f.write("<div class=\"word\">{}</div>".format(i.strip('%').rstrip('\n')))
                f.write("</details>\n")
            elif i.startswith("    "):
                f.write("<details>")
                f.write("<summary class=\"phrase\">{}</summary>\n".format(i.strip().rstrip('\n')))
            elif i.startswith("#"):
                f.write("<div class=\"translation\">{}</div>".format(i.strip('#').rstrip('\n')))
                f.write("</details>\n")
            elif i == '\n':
                f.write("</br>\n")

# version_2_GRE(rewrite_path=rewrite_path, write_path=write_path)

with open("version head GRE vocabulary.html", 'r', encoding="UTF-8") as f:
    c0 = f.read()
# with open("version 0.0 GRE vocabulary.html", 'r', encoding="UTF-8") as f:
#     c1 = f.readlines()
def parent_dir():
    # 获取当前Python文件所在的目录
    current_file_dir = os.path.abspath(os.path.dirname(__file__))
    
    # 获取当前文件的父目录
    parent_dir = os.path.dirname(current_file_dir)
    
    # 获取父目录的父目录（即当前文件的祖父目录）
    grandparent_dir = os.path.dirname(parent_dir)
    
    print("当前Python文件目录的前两个目录：")
    print(parent_dir)
    print(grandparent_dir)
    return parent_dir

GRE_dir =os.path.join(parent_dir(), "GRE vocabulary.html")
with open(GRE_dir, 'w', encoding="UTF-8") as f:
    f.write(c0)
    for i in range(21, 118):
        f.write("<hr id=\"Unit {}\"/>\n".format(i))
        f.write("<div class=\"totop\" >\n")
        f.write("    <a href=\"#top\">Back to top</a>\n")
        f.write("</div>\n")
        f.write("<h2>Unit {}</h2>\n".format(i))

        name = "Unit {}".format(i)
        rewrite_path = "{}.txt".format(name)
        version_2_GRE(rewrite_path=rewrite_path, write_path=write_path)
        with open(write_path, 'r', encoding="UTF-8") as f2:
            c2 = f2.read()
        f.write(c2)
        f.write("\n\n\n")
    f.write("<hr/>\n")
    f.write('\n')
    f.write("</div> <!-- class=\"box\"-->\n")
    f.write('\n')
    f.write("</body>\n")
=======
import re
import os

# read_path = "GRE vocabulary.txt"
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if u"\u4e00" <= uchar <= u"\u9fff":
        return True
    else:
        return False

name = "Unit 30"

read_path = "b {}.txt".format(name)
rewrite_path = "{}.txt".format(name)
write_path = "unit GRE vocabulary.html"

# # # # 1、
# my_re = re.compile(r'[A-Za-z]',re.S)
# with open(read_path, 'r', encoding="UTF-8") as f:
#     c = f.readlines()
# with open(rewrite_path, 'w', encoding="UTF-8") as f:
#     for i in c:
#         res_n = re.findall(my_re, i.rstrip('\n'))
#         decerator = False
#         for j in i:
#             if is_chinese(j[0]):
#                 decerator = '#'
#                 i = i.replace(' ', '').replace(',', '，').replace('.', '。').replace('(', '（').replace(')', '）'.replace(':', '：'))
#                 f.write('#'+i)
#                 break
#         if ' ' in i[:-2]:
#             i = i.replace(',', ', ').replace('  ', ' ')
#             f.write('    '+i)
#         elif res_n:
#             f.write(i.rstrip('\n').rstrip()+":\n")
#         elif i == '\n':
#             f.write(i)


# # # # 2、 version 1.0
# with open(rewrite_path, 'r', encoding="UTF-8") as f:
#     c = f.readlines()

# with open(write_path, 'w', encoding="UTF-8") as f:
#     c_len = 0
#     for i in c:
#         if i.endswith(":\n"):
#             c_len+=1
#     print(c_len)
#     num = 0
#     test_2 = True
#     for j,i in enumerate(c):
#         if i.endswith(":\n"):
#             num+=1
#         if num%10 == 1 and test_2:
#             if num//10 < c_len//10:
#                 f.write("<h5>{} - {}</h5>\n".format(num, num+9))
#             else:
#                 f.write("<h5>{} - {}</h5>\n".format(num, c_len))
#             test_2 = False
#         if num%10 == 2:
#             test_2 = True

#         if i.startswith("    "):
#             f.write("<a href=\"javascript:void(null);\" title=\"{}\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>{}</br>\n".format(c[j+1][1:-1], i.strip()))
#         elif i[0] != '#':
#             f.write(i.replace('\n', "</br>\n"))

# # # 2、 version 2.0
def version_2_GRE(rewrite_path, write_path):
    with open(rewrite_path, 'r', encoding="UTF-8") as f:
        c = f.readlines()

    with open(write_path, 'w', encoding="UTF-8") as f:
        c_len = 0
        for i in c:
            if i.endswith("]\n"):
                c_len+=1
        print(c_len)
        num = 0
        test_2 = True
        for j,i in enumerate(c):
            if i.endswith("]\n"):
                num+=1
            if num%10 == 1 and test_2:
                if num//10 < c_len//10:
                    f.write("<h5>{} - {}</h5>\n".format(num, num+9))
                else:
                    f.write("<h5>{} - {}</h5>\n".format(num, c_len))
                test_2 = False
            if num%10 == 2:
                test_2 = True

            if i.endswith("]\n"):
                f.write("<details><summary class=\"vocabulary\">\n")
                f.write("{} <span class=\"phonetic\">{}</span></summary>\n".format(i[:i.find(':')], i[i.find(':'):].rstrip('\n')))
            elif i.startswith("$"):
                f.write("<div class=\"word\">{}</div>".format(i.strip('$').rstrip('\n')))
                f.write("\n")
            elif i.startswith("%"):
                f.write("<div class=\"word\">{}</div>".format(i.strip('%').rstrip('\n')))
                f.write("</details>\n")
            elif i.startswith("    "):
                f.write("<details>")
                f.write("<summary class=\"phrase\">{}</summary>\n".format(i.strip().rstrip('\n')))
            elif i.startswith("#"):
                f.write("<div class=\"translation\">{}</div>".format(i.strip('#').rstrip('\n')))
                f.write("</details>\n")
            elif i == '\n':
                f.write("</br>\n")

# version_2_GRE(rewrite_path=rewrite_path, write_path=write_path)

with open("version head GRE vocabulary.html", 'r', encoding="UTF-8") as f:
    c0 = f.read()
# with open("version 0.0 GRE vocabulary.html", 'r', encoding="UTF-8") as f:
#     c1 = f.readlines()
def parent_dir():
    # 获取当前Python文件所在的目录
    current_file_dir = os.path.abspath(os.path.dirname(__file__))
    
    # 获取当前文件的父目录
    parent_dir = os.path.dirname(current_file_dir)
    
    # 获取父目录的父目录（即当前文件的祖父目录）
    grandparent_dir = os.path.dirname(parent_dir)
    
    print("当前Python文件目录的前两个目录：")
    print(parent_dir)
    print(grandparent_dir)
    return parent_dir

GRE_dir =os.path.join(parent_dir(), "GRE vocabulary.html")
with open(GRE_dir, 'w', encoding="UTF-8") as f:
    f.write(c0)
    for i in range(21, 118):
        f.write("<hr id=\"Unit {}\"/>\n".format(i))
        f.write("<div class=\"totop\" >\n")
        f.write("    <a href=\"#top\">Back to top</a>\n")
        f.write("</div>\n")
        f.write("<h2>Unit {}</h2>\n".format(i))

        name = "Unit {}".format(i)
        rewrite_path = "{}.txt".format(name)
        version_2_GRE(rewrite_path=rewrite_path, write_path=write_path)
        with open(write_path, 'r', encoding="UTF-8") as f2:
            c2 = f2.read()
        f.write(c2)
        f.write("\n\n\n")
    f.write("<hr/>\n")
    f.write('\n')
    f.write("</div> <!-- class=\"box\"-->\n")
    f.write('\n')
    f.write("</body>\n")
>>>>>>> 2ceae69a4c81ebe4802c098fe21191cdd0ee2b42
