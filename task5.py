# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
with open("task5.txt", "r", encoding="utf-8") as f:
    fail = f.read()
Slovo = fail.replace(".", "").replace(",", "").replace("!", "").split()
print(Slovo)
schetchik = ""
for drugoe_slovo in Slovo:
    if len(drugoe_slovo) > len(schetchik):
        schetchik = drugoe_slovo
bukov=len(schetchik)
with open("task5new", "w", encoding="utf-8") as filenovi:
    filenovi.write(f"{schetchik}\n")
    filenovi.write(f"{bukov}\n")
print(schetchik)
print(bukov)
