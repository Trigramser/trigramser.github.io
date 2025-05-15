<<<<<<< HEAD
# coding=utf-8
import io
import sys
import re
import requests
import chardet
import urllib.request
import urllib.parse
import json
import os

# =========================================
# 1、下载网页文件，根据网页文件生成下载目录
# =========================================

'''
    gbk' codec can't encode character '\xa9' in position 106949: illegal multibyte sequence编码异常
    网上试了很多方法,直到看到一位大佬说这种是win系统造成的编码错误,所以我把代码放到了linux上面运行,gbk编码异常解决了
    但是一直在linux上写代码,个人感觉不是很舒服,然后又找了半天,最终问题得以解决
    加入以下代码即可解决
'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

def youdao_trans(vocabulary):
    url = "https://www.youdao.com/result"
    headers = {
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
        "user-agent": "Mozilla/5.0 (Windows 98) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/60.0.861.0 Safari/532.2"
        
        
    }
    params = {
        "word": vocabulary,
        "lang": "en"
    }

    # params = urllib.parse.urlencode(params).encode("utf-8")
    # a = urllib.request.Request(url, params)
    # a = urllib.request.urlopen(a)
    # html = a.read().decode("utf-8")
    # print(html)

    resp = requests.get(url, params=params, headers=headers)
    resp.close()
    resp_text = resp.text
    resp_content = resp.content

    vocabulary_phonetic_en = r"<span data-v-8da1f94a>英</span><span class=\"phonetic\" data-v-8da1f94a>/ (?P<en>.*?) /</span><div class=\"phraseSpeech phonetic-speech\" data-v-9a937c9a data-v-8da1f94a>"
    vocabulary_phonetic_am = r"<span data-v-8da1f94a>美</span><span class=\"phonetic\" data-v-8da1f94a>/ (?P<am>.*?) /</span><div class=\"phraseSpeech phonetic-speech\" data-v-9a937c9a data-v-8da1f94a>"
    obj_phonetic_en = re.compile(vocabulary_phonetic_en)
    obj_phonetic_am = re.compile(vocabulary_phonetic_am)
    obj_iter_en = obj_phonetic_en.finditer(resp_text)
    obj_iter_am = obj_phonetic_am.finditer(resp_text)
    phonetic_list = []
    for i,k in zip(obj_iter_en, obj_iter_am):
        phonetic_list.append('英['+i.group("en")+']')
        phonetic_list.append('美['+k.group("am")+']')

    vocabulary_trans = r"<li class=\"word-exp\" data-v-d80c723c><span class=\"pos\" data-v-d80c723c>(?P<class>.*?)</span><span class=\"trans\" data-v-d80c723c>(?P<trans>.*?)</span>"
    # obj_class = re.compile(vocabulary_class)
    obj_trans = re.compile(vocabulary_trans)
    # obj_iter_class = obj_class.finditer(resp_text)
    obj_iter_trans = obj_trans.finditer(resp_text)
    class_list = []
    trans_list = []
    for i in obj_iter_trans:
        class_list.append(i.group("class"))
        # print(i.group("class"))
    # for i in obj_iter_trans:
        trans_list.append(i.group("trans").replace("&lt;", '<').replace("&gt;", '>'))
        # print(i.group("trans"))

    for i in phonetic_list:
        print(i)
    for i,k in zip(class_list, trans_list):
        print(i+' '+k)

    return [phonetic_list, class_list, trans_list]

# youdao_trans("pretentious")


def phonetic_unit(origin_path, rewrite_path):
    with open(origin_path, 'r', encoding="UTF-8") as f:
        c = f.readlines()
    with open(rewrite_path, 'w', encoding="UTF-8") as f:
        for j,i in enumerate(c):
            if i.endswith(":\n"):
                if not '(' in i:
                    word = i[:i.find(':')]
                    youdao_list = youdao_trans(word)
                else:
                    word = i[:i.find('(')]
                    youdao_list = youdao_trans(word)

                f.write(i.rstrip('\n'))
                for k in youdao_list[0]:
                    f.write(' '+k)
                f.write('\n')
                class_list_len = len(youdao_list[1])-1
                for n,[l,m] in enumerate(zip(youdao_list[1], youdao_list[2])):
                    if n<class_list_len:
                        f.write('$'+l+' '+m+'\n')
                    else:
                        f.write('%'+l+' '+m+'\n')
            else:
                f.write(i)

# origin_path = "p_Unit 21.txt"
# rewrite_path = "Unit 21.txt"
# phonetic_unit(origin_path, rewrite_path)
for i in range(21, 118):
    phonetic_unit(origin_path="p_Unit {}.txt".format(i), rewrite_path="Unit {}.txt".format(i))
    print("Unit {}.txt".format(i))

=======
# coding=utf-8
import io
import sys
import re
import requests
import chardet
import urllib.request
import urllib.parse
import json
import os

# =========================================
# 1、下载网页文件，根据网页文件生成下载目录
# =========================================

'''
    gbk' codec can't encode character '\xa9' in position 106949: illegal multibyte sequence编码异常
    网上试了很多方法,直到看到一位大佬说这种是win系统造成的编码错误,所以我把代码放到了linux上面运行,gbk编码异常解决了
    但是一直在linux上写代码,个人感觉不是很舒服,然后又找了半天,最终问题得以解决
    加入以下代码即可解决
'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

def youdao_trans(vocabulary):
    url = "https://www.youdao.com/result"
    headers = {
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
        "user-agent": "Mozilla/5.0 (Windows 98) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/60.0.861.0 Safari/532.2"
        
        
    }
    params = {
        "word": vocabulary,
        "lang": "en"
    }

    # params = urllib.parse.urlencode(params).encode("utf-8")
    # a = urllib.request.Request(url, params)
    # a = urllib.request.urlopen(a)
    # html = a.read().decode("utf-8")
    # print(html)

    resp = requests.get(url, params=params, headers=headers)
    resp.close()
    resp_text = resp.text
    resp_content = resp.content

    vocabulary_phonetic_en = r"<span data-v-8da1f94a>英</span><span class=\"phonetic\" data-v-8da1f94a>/ (?P<en>.*?) /</span><div class=\"phraseSpeech phonetic-speech\" data-v-9a937c9a data-v-8da1f94a>"
    vocabulary_phonetic_am = r"<span data-v-8da1f94a>美</span><span class=\"phonetic\" data-v-8da1f94a>/ (?P<am>.*?) /</span><div class=\"phraseSpeech phonetic-speech\" data-v-9a937c9a data-v-8da1f94a>"
    obj_phonetic_en = re.compile(vocabulary_phonetic_en)
    obj_phonetic_am = re.compile(vocabulary_phonetic_am)
    obj_iter_en = obj_phonetic_en.finditer(resp_text)
    obj_iter_am = obj_phonetic_am.finditer(resp_text)
    phonetic_list = []
    for i,k in zip(obj_iter_en, obj_iter_am):
        phonetic_list.append('英['+i.group("en")+']')
        phonetic_list.append('美['+k.group("am")+']')

    vocabulary_trans = r"<li class=\"word-exp\" data-v-d80c723c><span class=\"pos\" data-v-d80c723c>(?P<class>.*?)</span><span class=\"trans\" data-v-d80c723c>(?P<trans>.*?)</span>"
    # obj_class = re.compile(vocabulary_class)
    obj_trans = re.compile(vocabulary_trans)
    # obj_iter_class = obj_class.finditer(resp_text)
    obj_iter_trans = obj_trans.finditer(resp_text)
    class_list = []
    trans_list = []
    for i in obj_iter_trans:
        class_list.append(i.group("class"))
        # print(i.group("class"))
    # for i in obj_iter_trans:
        trans_list.append(i.group("trans").replace("&lt;", '<').replace("&gt;", '>'))
        # print(i.group("trans"))

    for i in phonetic_list:
        print(i)
    for i,k in zip(class_list, trans_list):
        print(i+' '+k)

    return [phonetic_list, class_list, trans_list]

# youdao_trans("pretentious")


def phonetic_unit(origin_path, rewrite_path):
    with open(origin_path, 'r', encoding="UTF-8") as f:
        c = f.readlines()
    with open(rewrite_path, 'w', encoding="UTF-8") as f:
        for j,i in enumerate(c):
            if i.endswith(":\n"):
                if not '(' in i:
                    word = i[:i.find(':')]
                    youdao_list = youdao_trans(word)
                else:
                    word = i[:i.find('(')]
                    youdao_list = youdao_trans(word)

                f.write(i.rstrip('\n'))
                for k in youdao_list[0]:
                    f.write(' '+k)
                f.write('\n')
                class_list_len = len(youdao_list[1])-1
                for n,[l,m] in enumerate(zip(youdao_list[1], youdao_list[2])):
                    if n<class_list_len:
                        f.write('$'+l+' '+m+'\n')
                    else:
                        f.write('%'+l+' '+m+'\n')
            else:
                f.write(i)

# origin_path = "p_Unit 21.txt"
# rewrite_path = "Unit 21.txt"
# phonetic_unit(origin_path, rewrite_path)
for i in range(21, 118):
    phonetic_unit(origin_path="p_Unit {}.txt".format(i), rewrite_path="Unit {}.txt".format(i))
    print("Unit {}.txt".format(i))

>>>>>>> 2ceae69a4c81ebe4802c098fe21191cdd0ee2b42
