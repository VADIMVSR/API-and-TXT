# Получаем значение N от пользователя
N = int(input("Введите максимальную длину строки: "))

# Открываем исходный файл и создаем файл для результата
with open('data.txt', 'r', encoding='utf-8') as infile, open('res.txt', 'w', encoding='utf-8') as outfile:
    # Читаем строки из файла
    for line in infile:
        # Если длина строки меньше N, записываем ее в выходной файл
        if len(line.strip()) < N:
            outfile.write(line)
