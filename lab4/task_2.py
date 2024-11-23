# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def line_separator(line_s, delimeter=',') -> list:
    # разбивает строку csv-файла на список
    line_s = line_s.rstrip()
    line_s = line_s.split(delimeter)
    return line_s

def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as f:
        keys = line_separator(f.readline())
        json_list = [dict(zip(keys, line_separator(linia))) for linia in f]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(json_list, f, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


