#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Кейс-задача № 3
Дан одномерный массив А размерности N.
Найти сумму отрицательных элементов, расположенных между максимальным и минимальным.
"""

import random


def find_sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов, расположенных между
    максимальным и минимальным элементами массива.
    """
    
    if not arr:
        print("Ошибка: массив пуст")
        return 0
    
    # Шаг 1: Находим индексы максимального и минимального элементов
    max_index = 0
    min_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
        if arr[i] < arr[min_index]:
            min_index = i
    
    # Шаг 2: Определяем границы интервала
    left = min(max_index, min_index)
    right = max(max_index, min_index)
    
    # Шаг 3: Суммируем отрицательные элементы между ними
    sum_negative = 0
    count_negative = 0
    
    for i in range(left + 1, right):
        if arr[i] < 0:
            sum_negative += arr[i]
            count_negative += 1
    
    # Шаг 4: Вывод информации
    print(f"Максимальный элемент: arr[{max_index}] = {arr[max_index]}")
    print(f"Минимальный элемент: arr[{min_index}] = {arr[min_index]}")
    print(f"Границы интервала: от индекса {left} до индекса {right}")
    print(f"Количество отрицательных элементов между ними: {count_negative}")
    print(f"Их сумма: {sum_negative}")
    
    return sum_negative


def generate_random_array(n, min_val=-50, max_val=50):
    """Генерирует массив случайных целых чисел."""
    return [random.randint(min_val, max_val) for _ in range(n)]


def main():
    """Основная функция программы."""
    
    # Ввод размерности массива
    while True:
        try:
            n = int(input("Введите размерность массива N (целое положительное число): "))
            if n <= 0:
                print("Размерность должна быть положительным числом. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")
    
    # Генерация и вывод массива
    arr = generate_random_array(n)
    print(f"\nСгенерированный массив A[{n}]:")
    print(arr)
    print()
    
    # Нахождение суммы
    result = find_sum_negative_between_min_max(arr)
    print(f"\nРезультат: сумма отрицательных элементов между максимумом и минимумом = {result}")


if __name__ == "__main__":
    main()
