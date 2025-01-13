# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
line_count = sum(1 for line in open("task1.txt"))
print("Строк" , line_count)
words = 0
symbols = 0
for line in open("task1.txt"):
    words += len(line.split())
    symbols += len(line.replace(' ', '')) 
print("Слов" , words)
print("Символов" , symbols) 
