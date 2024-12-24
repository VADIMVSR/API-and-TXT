import re

# Регулярное выражение для поиска текста в круглых скобках
pattern = r'\((.*?)\)'

# Открываем исходный файл и создаем файл для результата
with open('data3.txt', 'r', encoding='utf-8') as infile, open('res4.txt', 'w', encoding='utf-8') as outfile:
    # Перебираем строки по порядку
    for i, line in enumerate(infile, 1):
        # Ищем все совпадения по регулярному выражению
        matches = re.findall(pattern, line)
        # Если есть совпадения, записываем их в выходной файл с номером строки
        if matches:
            for match in matches:
                outfile.write(f"Строка {i}: {match}\n")
