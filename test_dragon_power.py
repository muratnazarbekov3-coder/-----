#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Тесты для кейс-задачи № 4
"""

import unittest


def max_dragon_power_dp(N):
    """Динамическое программирование"""
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
    """Оптимизированный алгоритм"""
    if N <= 0:
        return 0
    if N <= 7:
        return N
    
    result = 1
    while N > 4:
        result *= 3
        N -= 3
    
    if N == 4:
        result *= 4
    elif N == 3:
        result *= 3
    elif N == 2:
        result *= 2
    elif N == 1:
        result *= 1
    
    return result


class TestDragonPower(unittest.TestCase):
    
    def test_basic_cases(self):
        """Базовые случаи N <= 7"""
        for N in range(1, 8):
            with self.subTest(N=N):
                expected = N  # Один дракон с N головами
                self.assertEqual(max_dragon_power_optimized(N), expected)
    
    def test_small_cases(self):
        """Малые значения N > 7"""
        test_cases = [
            (8, 18),   # 3*3*2 = 18
            (9, 27),   # 3*3*3 = 27
            (10, 36),  # 3*3*4 = 36
            (11, 54),  # 3*3*3*2 = 54
            (12, 81),  # 3*3*3*3 = 81
            (13, 108), # 3*3*3*4 = 108
            (14, 162), # 3*3*4*4 = 162
            (15, 243), # 3*3*3*3*3 = 243
        ]
        
        for N, expected in test_cases:
            with self.subTest(N=N):
                result = max_dragon_power_optimized(N)
                self.assertEqual(result, expected, f"N={N}: {result} != {expected}")
    
    def test_comparison_methods(self):
        """Сравнение DP и оптимизированного алгоритма"""
        for N in range(1, 50):
            with self.subTest(N=N):
                dp = max_dragon_power_dp(N)
                opt = max_dragon_power_optimized(N)
                self.assertEqual(dp, opt, f"N={N}: DP={dp}, OPT={opt}")
    
    def test_growing_sequence(self):
        """Проверка монотонного роста"""
        prev = 0
        for N in range(1, 30):
            current = max_dragon_power_optimized(N)
            self.assertGreaterEqual(current, prev, f"N={N}: {current} < {prev}")
            prev = current
    
    def test_large_values(self):
        """Большие значения"""
        for N in [50, 80, 99]:
            with self.subTest(N=N):
                result = max_dragon_power_optimized(N)
                self.assertGreater(result, 0)
                print(f"N={N}, сила = {result}")


if __name__ == "__main__":
    print("=" * 50)
    print("Запуск тестов для драконьей стаи")
    print("=" * 50)
    print()
    unittest.main(verbosity=2)
