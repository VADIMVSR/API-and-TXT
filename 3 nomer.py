# Открываем исходный файл и создаем файл для результата
with open('data2.txt', 'r', encoding='utf-8') as infile, open('res2.txt', 'w', encoding='utf-8') as outfile:
    # Читаем строки из файла
    for line in infile:
        # Заменяем несколько пробелов одним
        cleaned_line = ' '.join(line.split())
        # Записываем результат в выходной файл
        outfile.write(cleaned_line + '\n')
