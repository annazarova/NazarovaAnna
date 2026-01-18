# TODO решите задачу
import json


def task() -> float:
    # Данные из файла input.json
    data = [
        {"score": 0.0009456152645028281, "weight": 1},
        {"score": 0.00020640167757499364, "weight": 1},
        {"score": 0, "weight": 1},
        {"score": 1.6557065217391307, "weight": 1},
        {"score": 0, "weight": 1},
        {"score": 0.6066065217391303, "weight": 1},
        {"score": 0.03126181644071977, "weight": 1},
        {"score": 0.001253973281817707, "weight": 1}
    ]

    total_sum = 0.0
    for item in data:
        total_sum += item["score"] * item["weight"]

    return round(total_sum, 3)


print(task())
