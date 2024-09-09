import numpy as np

def extract_features(key_data):
    hold_times = []
    flight_times = []
    key_data = eval(key_data)
    # Перебираем события нажатий и отпусканий клавиш
    for i in range(len(key_data) - 1):

        # {'key': 'Enter', 'eventType': 'keyup', 'timestamp': 1725815934459}
        current_event = key_data[i]
        next_event = key_data[i + 1]
        if current_event.get('key') == 'Enter':
            # print("Enter key was skipped!")
            continue

        if current_event['eventType'] == 'keydown' and next_event['eventType'] == 'keyup' and current_event['key'] == \
                next_event['key']:
            # Время удержания клавиши (разница между отпусканием и нажатием)
            hold_time = next_event['timestamp'] - current_event['timestamp']
            hold_times.append(hold_time)

        if current_event['eventType'] == 'keyup' and next_event['eventType'] == 'keydown':
            # Время между отпусканием одной клавиши и нажатием следующей (flight time)
            flight_time = next_event['timestamp'] - current_event['timestamp']
            flight_times.append(flight_time)

    # Агрегируем признаки (можно использовать различные статистические методы)
    features = {}
    if hold_times:
        features['hold_time_mean'] = np.mean(hold_times)
        features['hold_time_std'] = np.std(hold_times)
    else:
        features['hold_time_mean'] = 0
        features['hold_time_std'] = 0

    if flight_times:
        features['flight_time_mean'] = np.mean(flight_times)
        features['flight_time_std'] = np.std(flight_times)

    else:
        features['flight_time_mean'] = 0
        features['flight_time_std'] = 0

    return list(
        # output data format
        # [np.float64(151.0), np.float64(11.575836902790225), np.float64(135.0), np.float64(85.51315688243535)]
        features.values())