# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.

import os
import io

filename = "Phone book.txt"

def find():
    fstr = input('Введите поисковый запрос: ')
    found = False
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            if (fstr in line):
                found = True
                print(line)
        if (not found):
            print('Ничего не найдено')
        file.close()

def append():
    name = input('Введите имя: ')
    num = input('Введите номер: ')
    if (len(name) == 0 or len(num) == 0):
        print('Некорректный ввод')
    else:
        with open(filename, 'a', encoding='UTF-8') as file:
            file.write(name + '\t' + num + '\n')
            file.close()

def delete():
    fstr = input('Введите поисковый запрос: ')
    data = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            if (fstr not in map(str.strip, line.split('\t'))):
                data.append(line)
        file.close()
    
    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(data)
        file.close()

def edit():
    fstr = input('Введите поисковый запрос: ')
    found = []
    with open(filename, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for i, line in enumerate(data):
            if (fstr in line):
                found.append(i)
                print(str(len(found)) + ': ' + line, end='')
        file.close()
        
    if (len(found) > 0):
        nstr = int(input('Введите номер редактируемой строки: ')) - 1
        if (nstr < 0 or nstr >= len(found)):
            print('Некорректный ввод')
        else:
            name = input('Введите имя: ')
            num = input('Введите номер: ')
            if (len(name) == 0 or len(num) == 0):
                print('Некорректный ввод')
            else:
                data[found[nstr]] = name + '\t' + num + '\n'
                with open(filename, 'w', encoding='UTF-8') as file:
                    file.writelines(data)
                    file.close()
    else:
        print('Ничего не найдено')

def list():
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            print(line,end='')
        file.close()

def main(cmd):
    match cmd:
        case 'edit' | 'e':
            edit()
        case 'find' | 'f':
            find()
        case 'add' | 'a':
            append()
        case 'del' | 'd':
            delete()
        case 'exit' | 'x':
            exit()
        case 'list' | 'l':
            list()

while True:
    main(input('Введи команду (find(f)|edit(e)|add(a)|del(d)|exit(x)|list(l)): '))