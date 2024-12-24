import argparse

def count_lines(file_path):
    """Функция для подсчета количества строк в файле.

    Аргументы:
    file_path -- путь до текстового файла

    Возвращает:
    Количество строк в файле или 0 в случае ошибки
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def main():
    # Парсим аргументы командной строки
    parser = argparse.ArgumentParser(description="Подсчет количества строк в файле")
    parser.add_argument('--file', type=str, required=True, help='Имя текстового файла')

    args = parser.parse_args()

    # Получаем путь до файла и вызываем функцию для подсчета строк
    file_path = args.file
    line_count = count_lines(file_path)

    # Выводим результат на экран
    print(f"Количество строк в файле '{file_path}': {line_count}")

if __name__ == '__main__':
    main()
