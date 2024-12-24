# Функция для подсчета слов в строке
def count_words_in_line(line):
    # Убираем лишние пробелы по краям
    line = line.strip()
    # Разделяем строку по пробелам
    words = line.split()
    # Возвращаем количество слов
    return len(words)

# Открываем файл для чтения и файл для записи результата
with open('data1.txt', 'r', encoding='utf-8') as infile, open('res1.txt', 'w', encoding='utf-8') as outfile:
    # Перебираем строки по порядку
    for i, line in enumerate(infile, 1):
        # Считаем количество слов в строке
        word_count = count_words_in_line(line)
        # Записываем результат в файл res.txt
        outfile.write(f"Строка {i}: {word_count} слов\n")
    outfile.write(f"Всего строк: {i}")
