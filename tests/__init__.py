import unittest
import math
from main import RPNCalculator 

class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.calc = RPNCalculator()

    def print_test_result(self, expression, tokens, infix, result):
        """Вспомогательная функция для вывода результатов теста"""
        print(f"Выражение RPN: {expression}")
        print(f"Токены RPN: {tokens}")
        print(f"Инфиксная запись: {infix}")
        print(f"Результат вычисления: {result}")
        print("-" * 50)

    def test_simple_addition(self):
        """Тест простого сложения"""
        expression = "7 9 +"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 16)

    def test_complex_expression(self):
        """Тест сложного выражения с приоритетами"""
        expression = "34 7 0 + 5 * + 2 -"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 67)

    def test_power_operation(self):
        """Тест операции возведения в степень"""
        expression = "4 5 ^"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 1024)

    def test_division(self):
        """Тест деления"""
        expression = "25 5 /"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 5)

    def test_modulo_operation(self):
        """Тест операции modulo"""
        expression = "11 4 %"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 3)

    def test_sqrt_function(self):
        """Тест функции квадратного корня"""
        expression = "36 sqrt"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 6.0)

    def test_sin_function(self):
        """Тест функции синуса"""
        expression = "0 sin"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertAlmostEqual(result, 0.0, places=5)

    def test_pi_constant(self):
        """Тест константы pi"""
        expression = "pi 2 *"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertAlmostEqual(result, 2 * math.pi, places=5)

    def test_e_constant(self):
        """Тест константы e"""
        expression = "e 1 +"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertAlmostEqual(result, math.e + 1, places=5)

    def test_float_numbers(self):
        """Тест работы с дробными числами"""
        expression = "7.5 0.75 -"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 6.75)

    def test_combined_functions(self):
        """Тест комбинации функций"""
        expression = "2 sqrt 4 ^"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 4.000000000000001)

    def test_log_function(self):
        """Тест функции логарифма"""
        expression = "100 log"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 2.0)

    def test_abs_function(self):
        """Тест функции модуля"""
        expression = "6 abs"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, 6)

    def test_expression_with_all_operations(self):
        """Тест выражения со всеми операциями"""
        expression = "2 3 ^ 4 * 5 + 6 - 2 /"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertEqual(result, (2 ** 3 * 4 + 5 - 6) / 2, 15.5)

    def test_cos_function(self):
        """Тест функции косинуса"""
        expression = "0 cos"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_exp_function(self):
        """Тест экспоненциальной функции"""
        expression = "1 exp"
        tokens = self.calc.tokenize(expression)
        infix = self.calc.rpn_to_infix(tokens.copy())
        result = self.calc.evaluate_rpn(tokens)

        self.print_test_result(expression, tokens, infix, result)
        self.assertAlmostEqual(result, math.e, places=5)

    # Тесты ошибок

    def test_division_by_zero(self):
        """Тест деления на ноль"""
        expression = "5 0 /"
        tokens = self.calc.tokenize(expression)

        print(f"Выражение RPN: {expression}")
        print(f"Токены RPN: {tokens}")

        try:
            infix = self.calc.rpn_to_infix(tokens.copy())
            print(f"Инфиксная запись: {infix}")
            result = self.calc.evaluate_rpn(tokens)
            print(f"Результат вычисления: {result}")
        except Exception as e:
            print(f"Результат вычисления: Ошибка - {e}")
            result = f"Ошибка: {e}"

        self.assertTrue("Деление на ноль" in str(result) or "Ошибка" in str(result))

    def test_insufficient_operands(self):
        """Тест недостаточного количества операндов"""
        expression = "5 +"
        tokens = self.calc.tokenize(expression)

        print(f"Выражение RPN: {expression}")
        print(f"Токены RPN: {tokens}")

        try:
            infix = self.calc.rpn_to_infix(tokens.copy())
            print(f"Инфиксная запись: {infix}")
            result = self.calc.evaluate_rpn(tokens)
            print(f"Результат вычисления: {result}")
        except Exception as e:
            print(f"Результат вычисления: Ошибка - {e}")
            result = f"Ошибка: {e}"

        self.assertTrue("Недостаточно операндов" in str(result) or "Ошибка" in str(result))

    def test_invalid_character(self):
        """Тест невалидного символа"""
        expression = "5 4 @"

        print(f"Выражение RPN: {expression}")

        try:
            tokens = self.calc.tokenize(expression)
            print(f"Токены RPN: {tokens}")
            infix = self.calc.rpn_to_infix(tokens.copy())
            print(f"Инфиксная запись: {infix}")
            result = self.calc.evaluate_rpn(tokens)
            print(f"Результат вычисления: {result}")
        except Exception as e:
            print(f"Токены RPN: невозможно получить (ошибка токенизации)")
            print(f"Результат вычисления: Ошибка - {e}")
            result = f"Ошибка: {e}"

        self.assertTrue("Некорректный символ" in str(result) or "Ошибка" in str(result))

    def test_negative_power(self):
        """Тест возведения в отрицательную степень"""
        expression = "2 -1 ^"

        print(f"Выражение RPN: {expression}")

        try:
            tokens = self.calc.tokenize(expression)
            print(f"Токены RPN: {tokens}")
            infix = self.calc.rpn_to_infix(tokens.copy())
            print(f"Инфиксная запись: {infix}")
            result = self.calc.evaluate_rpn(tokens)
            print(f"Результат вычисления: {result}")
        except Exception as e:
            print(f"Результат вычисления: Ошибка - {e}")
            result = f"Ошибка: {e}"

        self.assertTrue("Отрицательная степень не поддерживается" in str(result) or "Ошибка" in str(result))

    def test_sqrt_negative_number(self):
        """Тест квадратного корня из отрицательного числа"""
        expression = "-4 sqrt"

        print(f"Выражение RPN: {expression}")

        try:
            tokens = self.calc.tokenize(expression)
            print(f"Токены RPN: {tokens}")
            infix = self.calc.rpn_to_infix(tokens.copy())
            print(f"Инфиксная запись: {infix}")
            result = self.calc.evaluate_rpn(tokens)
            print(f"Результат вычисления: {result}")
        except Exception as e:
            print(f"Результат вычисления: Ошибка - {e}")
            result = f"Ошибка: {e}"

        self.assertTrue("Ошибка" in str(result) or "math domain error" in str(result).lower())
      
if __name__ == '__main__':
    unittest.main(verbosity=2) # Запуск тестов с подробным выводом
