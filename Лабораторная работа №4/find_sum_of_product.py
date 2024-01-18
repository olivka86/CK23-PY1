# TODO решите задачу
import json

INPUT_FILE = "input.json"


def task(json_file: str) -> float:
    with open(json_file, 'r') as f:
        data = json.load(f)

    product_sum = sum(item["score"] * item["weight"] for item in data)
    sum_round = round(product_sum, 3)

    return sum_round


print(task(INPUT_FILE))
