# скрипт, который делает синтетические данные на основе реальных

import random
import copy
import ast
import os

from math import ceil


# Функция для создания синтетических данных
# вход d = [{'key': 'Enter', 'eventType': 'keyup', 'timestamp': 1725821219742},...]
def generate_synthetic_data(real_data, variation_factor=1.5):
    synthetic_data = copy.deepcopy(real_data)
    for event in synthetic_data:
        print(type(event))
        print(f"event = {event}")
        # Изменяем временные метки для симуляции другого пользователя
        diff = ceil(random.randint(-50, 50) * variation_factor)
        print(diff)
        event['timestamp'] += diff
    return f"{str(synthetic_data)}\n"


def process_file(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Файл {input_file} не найден")

    # Чтение исходных данных и запись синтетических данных
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'a') as f_out:
            for line in f_in:
                try:
                    # Безопасное преобразование строки в словарь
                    data = ast.literal_eval(line.strip())

                    # Генерация синтетических данных
                    synthetic_data = generate_synthetic_data(data)

                    # Запись синтетических данных в файл
                    f_out.write(f"{synthetic_data}")

                except (ValueError, SyntaxError) as e:
                    # Обработка ошибки преобразования строки в словарь
                    print(f"Ошибка обработки строки: {line.strip()}. Ошибка: {e}")

    except IOError as e:
        print(f"Ошибка при работе с файлами: {e}")


# Используем нашу функцию для обработки
input_file = "../SAMPLES/samples_luna_ok.txt"
output_file = "samples_luna_synth.txt"

process_file(input_file, output_file)
