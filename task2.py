# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
f = open("task2.txt", "r", encoding="utf-8")
fail = f.read()
print(fail)
new_fail = fail.replace("Python", "Питон")
print(new_fail)
s = fail.count("Питон")
f.close()
new_fail1 = open("new_file_for_task_2.txt", "w", encoding="utf-8")
new_fail1.write(new_fail)
new_fail1.close()

