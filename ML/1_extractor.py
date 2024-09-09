import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from ml_utils import extract_features


# Загрузка данных из файла с сэмплами
def _read_samples_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()  # Читаем все строки в список
        # Убираем символы новой строки (\n) в конце каждой строки
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []


# def extract_features_del(key_data):
#     hold_times = []
#     flight_times = []
#     key_data = eval(key_data)
#     # Перебираем события нажатий и отпусканий клавиш
#     for i in range(len(key_data) - 1):
#
#         # {'key': 'Enter', 'eventType': 'keyup', 'timestamp': 1725815934459}
#         current_event = key_data[i]
#         next_event = key_data[i + 1]
#         if current_event.get('key') == 'Enter':
#             # print("Enter key was skipped!")
#             continue
#
#         if current_event['eventType'] == 'keydown' and next_event['eventType'] == 'keyup' and current_event['key'] == \
#                 next_event['key']:
#             # Время удержания клавиши (разница между отпусканием и нажатием)
#             hold_time = next_event['timestamp'] - current_event['timestamp']
#             hold_times.append(hold_time)
#
#         if current_event['eventType'] == 'keyup' and next_event['eventType'] == 'keydown':
#             # Время между отпусканием одной клавиши и нажатием следующей (flight time)
#             flight_time = next_event['timestamp'] - current_event['timestamp']
#             flight_times.append(flight_time)
#
#     # Агрегируем признаки (можно использовать различные статистические методы)
#     features = {}
#     if hold_times:
#         features['hold_time_mean'] = np.mean(hold_times)
#         features['hold_time_std'] = np.std(hold_times)
#     else:
#         features['hold_time_mean'] = 0
#         features['hold_time_std'] = 0
#
#     if flight_times:
#         features['flight_time_mean'] = np.mean(flight_times)
#         features['flight_time_std'] = np.std(flight_times)
#
#     else:
#         features['flight_time_mean'] = 0
#         features['flight_time_std'] = 0
#
#     return list(
#         # output data format
#         # [np.float64(151.0), np.float64(11.575836902790225), np.float64(135.0), np.float64(85.51315688243535)]
#         features.values())


# ЗАГРУЗКА СЭМПЛОВ И ОБУЧЕНИЕ МОДЕЛИ
all_features_real = []
all_features_fake = []

# loading true user sample
samples_list_real = _read_samples_file('../SAMPLES/samples_luna_ok.txt')

for line in samples_list_real:
    features = extract_features(line)
    all_features_real.append(features)



# samples_list_fake = _read_samples_file('samples_luna_synth.txt')  # syntetic random sample
samples_list_fake = _read_samples_file('../SAMPLES/samples_luna_left.txt')  # left hand printed sample


for line in samples_list_fake:
    features = extract_features(line)
    all_features_fake.append(features)


# Обучение модели

# Шаг 1: Формируем выборку
X = np.array(all_features_real + all_features_fake)
print(f"len real = {len(all_features_real)} -- len fake = {len(all_features_fake)}")
y = np.array([1] * len(all_features_real) + [0] * len(all_features_fake))  # Метки: 1 - тру пользователь, 0 синтетический / другой

# Шаг 2: Разделение на обучающие и тестовые наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Размер обучающей выборки: {len(X_train)}")
print(f"Размер тестовой выборки: {len(X_test)}")

# Шаг 3: Обучение модели (например, Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)  # количество лесов
model.fit(X_train, y_train)


# Шаг 4: Оценка модели
y_pred = model.predict(X_test)

# Шаг 5: Вывод результатов
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Шаг 6: Сохранение модели
joblib.dump(model, 'model.pkl')  # Сохраняем модель в файл