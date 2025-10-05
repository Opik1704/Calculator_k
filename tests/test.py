"""
Unit-тесты для калькулятора
"""

import unittest
import math
import sys
import os
from typing import Any

# Добавляем путь к src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculatorBasic(unittest.TestCase):
    """
    БАзовые команды
    """
    def setUp(self) -> None:
        """Ничего не возвращает создает Калькулятор """
        self.calculator = Calculator()
    def test_calculate_basic_arithmetic(self) -> None:
        """
        Тестирует базовые арифметические операции.
        """
        test_cases = [
            ("7 + 8", 15),
            ("148 - 8", 140),
            ("5 * 5", 25),
            ("16 / 4", 4.0),
            #c несколькими действиями
            ("2 + 3 * 4", 14),
            ("(2 + 3) * 4", 20),
            ("15 / 5 + 3",6.0)
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result: Any = self.calculator.calculate(expression)
                self.assertEqual(result, expected)
    
    def test_calculate_power_operations(self) -> None:
        """ Тест возведения в стеепень """
        test_cases = [
            ("2 ** 5", 32),
            ("5 ** 2", 25),
        ]
        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result: Any = self.calculator.calculate(expression)
                self.assertEqual(result, expected)
    def test_division_by_zero_raises_error(self) -> None:
        """Тест на не деления на  0"""
        with self.assertRaises(ValueError, msg="Деление на ноль"):
            self.calculator.calculate("5 / 0")
class TestCalculatorVariables(unittest.TestCase):
    """ Тесты для переменных """
    def setUp(self) -> None:
        """Ничего не возвращает создает Калькулятор """
        self.calculator = Calculator()
    
    def test_unknown_variable_raises_error(self) -> None:
        """
        Тестирует обработку неизвестной переменной.
        """
        with self.assertRaises(ValueError, msg="Неизвестная переменная"):
            self.calculator.calculate("unknown_var + 5")


class TestCalculatorFunctions(unittest.TestCase):
    """
    Тесты функций калькулятора.
    """
    
    def setUp(self) -> None:
        """Ничего не возвращает создает Калькулятор """
        self.calculator = Calculator()
    
    def test_basic_functions(self) -> None:
        """
        Тестирует базовые математические функции.
        """
        test_cases = [
            ("abs(-7)", 7),
            ("abs(4)", 4),
            ("sqrt(36)", 6),
            ("pow(2, 5)", 32),
            ("max(15, 1055, 148)", 1055),
            ("min(0, 15, 13)", 0),
            ("min(-5, 5, -10,15)", -10),
        ]
        
        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result: Any = self.calculator.calculate(expression)
                self.assertEqual(result, expected)
    
    def test_unknown_function_raises_error(self) -> None:
        """Проверка неизвестной функции  """
        with self.assertRaises(ValueError, msg="Неизвестная функция"):
            self.calculator.calculate("unknown_func(5)")
if __name__ == '__main__':
    unittest.main()
