#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного 
#минимума и не больше заданного максимума).

arr_inp = [1, 6, 67, 3, 5, 12]
arr_otp = []
min = 3
max = 10

for i, el in enumerate(arr_inp):
    if(el >= min and el <= max):
        arr_otp.append(i)

print(arr_otp)