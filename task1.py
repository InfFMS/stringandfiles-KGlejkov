# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
line = sum(1 for line in open("task1.txt"))
print("Строк:" , line)
slova = 0
simvoli = 0
for i in open("task1.txt", encoding="utf-8"):
    slova += len(i.split())
    simvoli += len(i)
print("Слов:" , slova-1)
print("Символов:" , simvoli)
