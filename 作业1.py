#encoding:utf-8

import re
dict = {}
def quanwen(a):
    with open(a) as file:
        neirong = file.read()
        return neirong

b = quanwen('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/太空旅客.txt')

def shuru(a):
    with open(a) as file:
        for line in file.readlines():
            line = re.sub('\n', '',line)
            list = re.findall(line,b)
            a = len(list)
            dict[line] = a
    with open('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/作业.txt','w') as writeFile:
        for line in dict:
            writeFile.write(line)
            writeFile.write(' ')
            writeFile.write('出现次数：')
            writeFile.write(str(dict[line]))
            writeFile.write('\n')
shuru('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/词典/角色/反派.txt')
shuru('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/词典/角色/角色.txt')
shuru('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/词典/角色/角色中的其他.txt')
shuru('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/词典/角色/男主角.txt')
shuru('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/词典/角色/女主角.txt')
shuru('/home/yangfan/下载/数挖2017培训教学资料/week2 Python基础语言讲解/作业/词典/角色/配角.txt')
