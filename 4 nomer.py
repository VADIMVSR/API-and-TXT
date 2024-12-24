import csv

# Получаем фамилию автора от пользователя
author_surname = input("Введите фамилию автора: ")

# Открываем исходный CSV файл и создаем файл для результата
with open('data.csv', 'r', encoding='utf-8') as csvfile, open('res3.txt', 'w', encoding='utf-8') as outfile:
    # Читаем CSV файл
    reader = csv.reader(csvfile)

    # Перебираем строки CSV файла
    for row in reader:
        # Ожидается, что структура CSV: [Фамилия автора, Название книги, Год издания]
        author, title, year = row
        year = int(year)  # Преобразуем год в число

        # Проверяем фамилию автора и год издания
        if author == author_surname and year < 2019:
            # Записываем название книги в файл res.txt
            outfile.write(title + '\t')
            year=str(year)
            outfile.write(year+'\n')
