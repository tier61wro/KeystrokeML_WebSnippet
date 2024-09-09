import os
import sys

import joblib
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ML.ml_utils import extract_features

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для всех маршрутов

# Загрузка модели
model = joblib.load('../ML/model.pkl')

def save_sample_data(key_data):
    with open('samples.txt', 'a') as f:
        f.write(f"{key_data}\n")

# Сбор информации о пользователе
@app.route('/collect', methods=['POST'])
def collect_data():
    data = request.json
    print('Received user data:', data)
    return jsonify({'status': 'success', 'message': 'User data received'}), 200


# Конец, который принимает символы введенные пользователем
@app.route('/keystroke', methods=['POST'])
def collect_keystroke_data():
    keystroke_data = request.json
    # for e in keystroke_data:
    #     print(f"{e.get('key')} -- {e.get('eventType')}")

    print('Received keystroke data:', keystroke_data)
    save_sample_data(keystroke_data)

    # Извлекаем признаки из полученных данных
    keystroke_data_str = str(keystroke_data)
    features = extract_features(keystroke_data_str)
    features = np.array(features).reshape(1, -1)  # Преобразуем в нужный формат для модели

    # Делаем предсказание с использованием модели
    prediction = model.predict(features)

    # Выводим результат предсказания
    if prediction == 1:
        result = 'Original user'
    else:
        result = 'Different user'

    print(f"User check is over, we have: {result}")
    return jsonify({'status': 'success', 'message': 'Keystroke data received', 'prediction': result}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
