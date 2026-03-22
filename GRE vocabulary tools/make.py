<<<<<<< HEAD


# for i in range(42, 118):
#     file = open("raw Unit {}.txt".format(i), mode='w')
#     file.close()

# #批量修改文件名
# #批量修改图片文件名
# import os

# filelist = os.listdir()
# print(filelist)

# for i in filelist:
#     if i.startswith("Unit"):
#         os.rename(i, "b "+i)
with open("version 0.0.html", mode='w', encoding="UTF-8") as f:
    for i in range(21, 118):
        f.write("<hr id=\"Unit {}\"/>\n".format(i))
        f.write("<div class=\"totop\" >\n")
        f.write("    <a href=\"#top\">Back to top</a>\n")
        f.write("</div>\n")
        f.write("<h2>Unit {}</h2>\n".format(i))
        f.write("\n\n\n")
=======


# for i in range(42, 118):
#     file = open("raw Unit {}.txt".format(i), mode='w')
#     file.close()

# #批量修改文件名
# #批量修改图片文件名
# import os

# filelist = os.listdir()
# print(filelist)

# for i in filelist:
#     if i.startswith("Unit"):
#         os.rename(i, "b "+i)
with open("version 0.0.html", mode='w', encoding="UTF-8") as f:
    for i in range(21, 118):
        f.write("<hr id=\"Unit {}\"/>\n".format(i))
        f.write("<div class=\"totop\" >\n")
        f.write("    <a href=\"#top\">Back to top</a>\n")
        f.write("</div>\n")
        f.write("<h2>Unit {}</h2>\n".format(i))
        f.write("\n\n\n")
>>>>>>> 2ceae69a4c81ebe4802c098fe21191cdd0ee2b42
