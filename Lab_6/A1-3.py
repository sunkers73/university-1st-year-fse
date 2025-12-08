import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def load_users_data():
    users_tree = ET.parse('users.xml')
    users = []
    for user_elem in users_tree.getroot().findall('user'):
        user = {
        'user_id': int(user_elem.find('user_id').text),
        'name': user_elem.find('name').text,
        'age': int(user_elem.find('age').text),
        'weight': int(user_elem.find('weight').text),
        'fitness_level': user_elem.find('fitness_level').text
        }

        workouts = []
        workouts_data = load_workouts_data()
        for workout in workouts_data:
            if workout['user_id'] == user['user_id']:
                workouts.append(workout)
        user['workouts'] = workouts
        users.append(user)
    return users

def load_workouts_data():
    workouts_tree = ET.parse('workouts.xml')
    workouts = []
    for workout in workouts_tree.getroot().findall('workout'):
        workout = {
            'user_id': int(workout.find('user_id').text),
            'workout_id': int(workout.find('workout_id').text),
            'date': workout.find('date').text,
            'type': workout.find('type').text,
            'duration': int(workout.find('duration').text),
            'distance': float(workout.find('distance').text),
            'calories': int(workout.find('calories').text),
            'avg_heart_rate': int(workout.find('avg_heart_rate').text),
            'intensity': workout.find('intensity').text,
        }
        workouts.append(workout)
    return workouts

def get_stats(users, workouts):
    total_users = len(users)
    total_workouts = len(workouts)
    total_duration = 0
    total_distance = 0
    total_calories = 0
    for workout_elem in workouts:
        total_duration += workout_elem['duration'] / 60
        total_distance += workout_elem['distance']
        total_calories += workout_elem['calories']
    stats = {
        'total_users': total_users,
        'total_workouts': total_workouts,
        'total_duration': total_duration,
        'total_distance': total_distance,
        'total_calories': total_calories,
    }

    print(f"\nОБЩАЯ СТАТИСТИКА")
    print(f"============================")
    print(f"Всего пользователей: {stats['total_users']}")
    print(f"Всего тренировок: {stats['total_workouts']}")
    print(f"Общее время: {stats['total_duration']:.1f} часов")
    print(f"Пройдено дистанции: {stats['total_distance']:.1f} км")
    print(f"Сожжено каллорий: {stats['total_calories']}\n")
    return stats

def analyze_user_activity(users):
    users_activity = []
    for user in users:
        total_workouts = len(user['workouts'])
        total_duration = 0
        total_calories = 0
        for workout in user['workouts']:
            total_duration += workout['duration'] / 60
            total_calories += workout['calories']
        user = {
            'user_name': user['name'],
            'fitness_level': user['fitness_level'],
            'total_workouts': total_workouts,
            'total_duration': total_duration,
            'total_calories': total_calories,
        }
        users_activity.append(user)
    users_activity_sorted = sorted(users_activity, key=lambda x: x['total_workouts'], reverse=True)

    print(f"\nТОП 3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЯ")
    for index, user in enumerate((users_activity_sorted[:3]), start=1):
        print(f"\t{index}. {user['user_name']} ({user['fitness_level']}):")
        print(f"\t\tТренировок: {user['total_workouts']}")
        print(f"\t\tВремя: {user['total_duration']:.1f} часов")
        print(f"\t\tКалорий: {user['total_calories']}\n")
    return users_activity_sorted

def analyze_workout_types(workouts):
    workout_types = []
    types = ["велосипед", "бег", "ходьба", "плавание", "силовая тренировка"]
    for type in types:
        total_workouts = 0
        total_duration = 0
        total_calories = 0
        for workout in workouts:
            if workout['type'] == type:
                total_workouts += 1
                total_duration += workout['duration']
                total_calories += workout['calories']
        workout = {
            'type': type,
            'total_workouts': total_workouts,
            'percentage': total_workouts / len(workouts) * 100,
            'average_duration': total_duration / total_workouts,
            'average_calories': total_calories / total_workouts,
        }
        workout_types.append(workout)

    print("\nРАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК")
    for workout_type in workout_types:
        print(f"\t{workout_type['type']}: {workout_type['total_workouts']} тренировок ({workout_type['percentage']:.1f}%)")
        print(f"\t\tсредняя длительность: {workout_type['average_duration']:.0f} мин")
        print(f"\t\tсредние калории: {workout_type['average_calories']:.0f} ккал\n")
    return workout_types

def find_user_workouts(user_name):
    for user in users:
        if user_name == user['name']:
            return user['workouts']

def analyze_user(user_name):
    for user in users:
        if user_name == user['name']:
            user = user
            break
    total_distance = 0
    total_duration = 0
    total_calories = 0
    for workout in user['workouts']:
        total_distance += workout['distance']
        total_duration += workout['duration'] / 60
        total_calories += workout['calories']
    user_statistics = {
        'user_name': user['name'],
        'age': user['age'],
        'weight': user['weight'],
        'fitness_level': user['fitness_level'],
        'total_workouts': len(user['workouts']),
        'total_distance': total_distance,
        'total_duration': total_duration,
        'total_calories': total_calories,
        'average_calories': total_calories / len(user['workouts']),
        'favorite_wokrout': max(user['workouts'], key=lambda w: w['type'])['type']
    }

    print(f"\nДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user_statistics['user_name']}")
    print(f"========================================")
    print(f"Возраст: {user_statistics['age']} лет, Вес: {user_statistics['weight']} кг")
    print(f"Уровень: {user_statistics['fitness_level']}")
    print(f"Тренировок: {user_statistics['total_workouts']}")
    print(f"Пройдено дистанции: {user_statistics['total_distance']:.1f} км")
    print(f"Общее время: {user_statistics['total_duration']:.1f} часов")
    print(f"Сожжено калорий: {user_statistics['total_calories']}")
    print(f"Средние калории за тренировку: {user_statistics['average_calories']:.0f}")
    print(f"Любимый тип тренировки: {user_statistics['favorite_wokrout']}")
    return user_statistics


users = load_users_data()
workouts = load_workouts_data()
stats = get_stats(users, workouts)
user_activity = analyze_user_activity(users)
workout_types = analyze_workout_types(workouts)
user_statistics = analyze_user('Борис')


def pie_chart_workout_types():
    labels = [item['type'] for item in workout_types]
    values = [item['total_workouts'] for item in workout_types]
    plt.title("Распределение тренировок по типам")
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.show()

def user_activity_bar_chart():
    names = [item["user_name"] for item in user_activity]
    values = [item["total_workouts"] for item in user_activity]
    plt.figure(figsize=(12, 5))
    bars = plt.bar(names, values)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, f"{int(height)}", ha="center")
    plt.title("Активность пользователей (количество тренировок)")
    plt.xlabel("Пользователи")
    plt.ylabel("Количество тренировок")
    plt.show()

def bar_chart_training_effectiveness():
    labels = [item["type"] for item in workout_types]
    efficiency = [item["average_calories"] / item["average_duration"] for item in workout_types]
    plt.figure(figsize=(12, 5))
    bars = plt.bar(labels, efficiency)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, f"{height:.2f}", ha="center")
    plt.title("Эффективность тренировок (калории/минуту)")
    plt.xlabel("Тип тренировки")
    plt.ylabel("Калории в минуту")
    plt.show()


def user_comparison_chart():
    names = []
    calories = []
    levels = []
    for user in user_activity:
        names.append(user['user_name'])
        calories.append(user['total_calories'])
        level = user['fitness_level']
        levels.append(level)
    color_map = {"начальный": "green", "средний": "yellow", "продвинутый": "red"}
    colors = [color_map.get(level) for level in levels]
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, calories, color=colors)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 50, height, ha='center')
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=color_map["начальный"], label='Начальный'),
        Patch(facecolor=color_map["средний"], label='Средний'),
        Patch(facecolor=color_map["продвинутый"], label='Продвинутый')
    ]
    plt.legend(handles=legend_elements)
    plt.title('Сравнение пользователей по общим затраченным калориям')
    plt.xlabel('Пользователи')
    plt.ylabel('Общие калории')
    plt.xticks(rotation=45)
    plt.show()


pie_chart_workout_types()
user_activity_bar_chart()
bar_chart_training_effectiveness()
user_comparison_chart()


