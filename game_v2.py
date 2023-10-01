"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска. 
    С каждым шагом диапазон поиска уменьшается в два раза. 
    Сложность алгоритма O(log N). Для 100 вариантов получаем не более 7 итераций.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left_bound, right_bound = 1, 101

    while True:
        count += 1

        # предполагаемое число
        predict_number = (right_bound + left_bound) // 2

        # если угодали, то выходим из цикла
        if number == predict_number:
            break
        # если загаданное число больше, то "подвигаем" левую границу, иначе - правую
        elif number > predict_number:
            left_bound = predict_number
        else:
            right_bound = predict_number

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток!")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
