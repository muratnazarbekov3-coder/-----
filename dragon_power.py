#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Кейс-задача № 4
Максимальная сила драконьей стаи

Дано: N - суммарное количество голов (0 < N < 100)
У каждого дракона от 1 до 7 голов
Нужно найти максимальное произведение количества голов драконов
"""


def max_dragon_power_dp(N):
    """
    Динамическое программирование (эталонный алгоритм)
    """
    if N <= 0:
        return 0
    if N <= 7:
        return N
    
    dp = [0] * (N + 1)
    for i in range(1, min(N, 7) + 1):
        dp[i] = i
    
    for i in range(2, N + 1):
        for heads in range(2, min(i, 7) + 1):
            if heads == i:
                dp[i] = max(dp[i], heads)
            else:
                dp[i] = max(dp[i], heads * dp[i - heads])
    
    return dp[N]


def max_dragon_power_optimized(N):
    """
    Оптимизированное решение на основе жадного алгоритма
    
    Стратегия:
    - Используем как можно больше драконов с 3 головами
    - Остаток 1 заменяем на 2+2
    - Остаток 2 оставляем как 2
    
    Сложность: O(log N), память: O(1)
    """
    if N <= 0:
        return 0
    if N <= 7:
        return N
    
    result = 1
    
    # Жадный алгоритм: используем 3, где возможно
    while N > 4:
        result *= 3
        N -= 3
    
    # Обработка остатка
    if N == 4:
        result *= 4
    elif N == 3:
        result *= 3
    elif N == 2:
        result *= 2
    elif N == 1:
        result *= 1
    
    return result


def find_optimal_split(N):
    """
    Находит оптимальное разбиение N на части (для вывода)
    """
    if N <= 7:
        return [N]
    
    parts = []
    while N > 4:
        parts.append(3)
        N -= 3
    
    if N == 4:
        parts.append(4)
    elif N == 3:
        parts.append(3)
    elif N == 2:
        parts.append(2)
    elif N == 1:
        parts.append(1)
    
    return parts


def main():
    """Основная функция программы"""
    
    print("=" * 60)
    print("Максимальная сила драконьей стаи")
    print("=" * 60)
    print()
    
    # Ввод данных
    while True:
        try:
            N = int(input("Введите суммарное количество голов N (0 < N < 100): "))
            if N <= 0 or N >= 100:
                print("Ошибка: N должно быть в диапазоне 0 < N < 100")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число")
    
    print()
    print(f"Входные данные: N = {N}")
    print()
    
    # Вычисление
    result_dp = max_dragon_power_dp(N)
    result_opt = max_dragon_power_optimized(N)
    
    print("Результаты:")
    print(f"  Динамическое программирование: {result_dp}")
    print(f"  Оптимизированный алгоритм:     {result_opt}")
    print()
    
    # Вывод оптимального разбиения
    parts = find_optimal_split(N)
    print("Оптимальное разбиение:")
    print(f"  {' + '.join(map(str, parts))} = {sum(parts)}")
    print(f"  Количество драконов: {len(parts)}")
    print()
    
    # Формула силы
    print("Формула:")
    if len(parts) > 1:
        print(f"  {' * '.join(map(str, parts))} = {result_opt}")
    else:
        print(f"  Один дракон с {N} головами")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
