# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import re
mas={}
fail=open("task3.txt", encoding="utf-8")
i=fail.read()
me=i.lower()
i=re.split(r"[ .,\n]+",me)
you=i.sort()
a=1
for j in range(1,len(i)):
    if i[j]==i[j-1]:
        a+=1
    if i[j]!=i[j-1]:
        mas[i[j-1]]=a
        count = 1
mas.pop("")
fail.close()
otv=str(mas)
Mas=otv[1:-1:].replace(", ","\n")

vspomogashka=open("task3new1.txt","x",encoding="utf-8")
i=vspomogashka.write(Mas)
vspomogashka.close()
