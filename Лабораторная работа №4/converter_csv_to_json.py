# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file: str, json_file: str) -> None:
    data = []
    with open(csv_file, 'r') as f:
        for row in csv.DictReader(f):
            data.append(row)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
