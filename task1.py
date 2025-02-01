# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open("task1.txt", 'r', encoding="utf-8") as f:
    fail = f.read()
strok = fail.splitlines()
strok_otv = len(strok)

with open("task1new.txt", "w", encoding="utf-8") as filevspomogashka:
    filevspomogashka.write(fail.replace("—", " "))
with open("task1new.txt", "r", encoding="utf-8") as filevspomogashka:
    slov = filevspomogashka.read()
slovotv = len(slov.split())
simvolov = len(fail)
print("Строк:" , strok_otv)
print("Слов:" , slovotv)
print("Символов:" , simvolov)
