import operator
import math


class RPNCalculator:
    def __init__(self):
        # Определяем поддерживаемые операторы и функции
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow,
            '%': operator.mod
        }

        # Унарные операции и функции
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'log': math.log10,
            'ln': math.log,
            'exp': math.exp,
            'abs': abs,
            'floor': math.floor,
            'ceil': math.ceil
        }

        # Константы
        self.constants = {
            'pi': math.pi,
            'e': math.e
        }

        # Приоритеты операторов для преобразования в инфиксную запись
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3
        }

    def tokenize(self, expression):
        """
        Разбивает выражение в RPN на токены.
        Поддерживает числа, операторы, функции и константы.
        """
        tokens = []
        i = 0
        n = len(expression)

        while i < n:
            char = expression[i]

            # Пропускаем пробелы
            if char.isspace():
                i += 1
                continue

            # Обработка чисел (целых и дробных)
            if char.isdigit() or char == '.':
                j = i
                # Собираем все цифры и точки, составляющие число
                while j < n and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                number_str = expression[i:j]

                # Проверяем, является ли токен валидным числом
                try:
                    if '.' in number_str:
                        token = float(number_str)
                    else:
                        token = int(number_str)
                    tokens.append(token)
                except ValueError:
                    raise ValueError(f"Некорректное число: {number_str}")

                i = j

            # Обработка функций и констант (буквенные идентификаторы)
            elif char.isalpha():
                j = i
                while j < n and (expression[j].isalpha() or expression[j] == '_'):
                    j += 1
                identifier = expression[i:j]

                # Проверяем, является ли идентификатор функцией или константой
                if identifier in self.functions:
                    tokens.append(identifier)
                elif identifier in self.constants:
                    tokens.append(self.constants[identifier])
                else:
                    raise ValueError(f"Неизвестная функция или константа: {identifier}")

                i = j

            # Обработка операторов
            elif char in self.operators:
                tokens.append(char)
                i += 1

            else:
                raise ValueError(f"Некорректный символ: {char}")

        return tokens

    def rpn_to_infix(self, rpn_tokens):
        """
        Преобразует выражение из RPN в инфиксную запись
        """
        stack = []

        for token in rpn_tokens:
            if isinstance(token, (int, float)):
                # Числа просто добавляем в стек как строки
                if isinstance(token, float) and token.is_integer():
                    stack.append(str(int(token)))
                else:
                    stack.append(str(token))

            elif token in self.functions:
                # Унарные функции
                if len(stack) < 1:
                    raise ValueError(f"Недостаточно операндов для функции '{token}'")

                operand = stack.pop()
                # Для функций добавляем скобки вокруг аргумента
                stack.append(f"{token}({operand})")

            elif token in self.operators:
                # Бинарные операторы
                if len(stack) < 2:
                    raise ValueError(f"Недостаточно операндов для оператора '{token}'")

                right = stack.pop()
                left = stack.pop()

                # Определяем приоритеты для расстановки скобок
                left_prec = self._get_operator_precedence(left)
                right_prec = self._get_operator_precedence(right)
                current_prec = self.precedence[token]

                # Добавляем скобки если нужно
                if left_prec is not None and left_prec < current_prec:
                    left = f"({left})"

                # Особые случаи для операторов с правой ассоциативностью
                if token == '^':
                    if right_prec is not None and right_prec <= current_prec:
                        right = f"({right})"
                else:
                    if right_prec is not None and right_prec < current_prec:
                        right = f"({right})"

                stack.append(f"{left} {token} {right}")

        if len(stack) != 1:
            raise ValueError("Некорректное выражение RPN")

        return stack[0]

    def _get_operator_precedence(self, expression):
        """
        Определяет приоритет оператора в выражении
        """
        # Если выражение в скобках - убираем внешние скобки
        expr = expression.strip()
        if expr.startswith('(') and expr.endswith(')'):
            # Проверяем сбалансированность скобок
            bracket_count = 0
            for i, char in enumerate(expr):
                if char == '(':
                    bracket_count += 1
                elif char == ')':
                    bracket_count -= 1
                    if bracket_count == 0 and i != len(expr) - 1:
                        break
            else:
                if bracket_count == 0:
                    return self._get_operator_precedence(expr[1:-1])

        # Ищем оператор с наименьшим приоритетом (не в скобках)
        min_precedence = None
        bracket_count = 0

        # Проходим с конца для правильного определения ассоциативности
        for i in range(len(expr) - 1, -1, -1):
            char = expr[i]
            if char == ')':
                bracket_count += 1
            elif char == '(':
                bracket_count -= 1
            elif bracket_count == 0 and char in self.precedence:
                prec = self.precedence[char]
                if min_precedence is None or prec < min_precedence:
                    min_precedence = prec

        return min_precedence

    def evaluate_rpn(self, rpn_tokens):
        """
        Вычисляет значение выражения в обратной польской нотации
        """
        stack = []

        for i, token in enumerate(rpn_tokens):
            # Если токен - число, помещаем в стек
            if isinstance(token, (int, float)):
                stack.append(token)

            # Если токен - оператор
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError(f"Недостаточно операндов для оператора '{token}'")

                # Извлекаем два последних операнда
                b = stack.pop()
                a = stack.pop()

                # Выполняем операцию и помещаем результат в стек
                try:
                    if token == '/' and b == 0:
                        raise ZeroDivisionError("Деление на ноль")
                    result = self.operators[token](a, b)
                    stack.append(result)
                except Exception as e:
                    raise ValueError(f"Ошибка при выполнении операции {a} {token} {b}: {e}")

            # Если токен - функция
            elif token in self.functions:
                if len(stack) < 1:
                    raise ValueError(f"Недостаточно операндов для функции '{token}'")

                # Извлекаем операнд
                x = stack.pop()

                # Выполняем функцию и помещаем результат в стек
                try:
                    result = self.functions[token](x)
                    stack.append(result)
                except Exception as e:
                    raise ValueError(f"Ошибка при выполнении функции {token}({x}): {e}")

        if len(stack) != 1:
            raise ValueError(f"Некорректное выражение. В стеке осталось {len(stack)} элементов: {stack}")

        return stack[0]

    def calculate(self, expression):
        """
        Основной метод для вычисления выражения в RPN
        """
        try:
            # Шаг 1: Токенизация
            tokens = self.tokenize(expression)
            print(f"Токены RPN: {tokens}")

            # Шаг 2: Преобразование в инфиксную запись
            infix_expression = self.rpn_to_infix(tokens.copy())
            print(f"Инфиксная запись: {infix_expression}")

            # Шаг 3: Вычисление
            result = self.evaluate_rpn(tokens)

            return result

        except Exception as e:
            return f"Ошибка: {e}"


def main():
    calculator = RPNCalculator()

    print("Калькулятор обратной польской нотации (RPN)")
    print("Доступные команды: help, exit")
    print("Введите выражение в RPN формате (например: '3 4 + 2 *')")

    while True:
        try:
            expression = input("\nRPN> ").strip()

            if expression.lower() in ['exit', 'quit', 'выход']:
                print("До свидания!")
                break
            elif expression.lower() in ['help', 'справка']:
                print("\nДоступные операторы: +, -, *, /, ^, %")
                print("Доступные функции: sin, cos, tan, sqrt, log, ln, exp, abs, floor, ceil")
                print("Константы: pi, e")
                print("Пример: 3 4 + 2 * => (3 + 4) * 2 = 14")
                continue
            elif expression == '':
                continue

            result = calculator.calculate(expression)
            print(f"Результат: {result}")

        except KeyboardInterrupt:
            print("\n\nДо свидания!")
            break
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
