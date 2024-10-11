def calculate(res):
    try:
        parts = res.split()
        if len(parts) != 3:
            raise ValueError("Ошибка ввода.")
        op1, operator   , op2 = parts
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Ошибка ввода оператора.")
        if not (op1.isdigit() and op2.isdigit()):
            raise ValueError("Введите числа")
        op1 = int(op1)
        op2 = int(op2)
        if not (1 <= op1 <= 10 and 1 <= op2 <= 10):
            raise ValueError("Введите целое число от 1 до 10")
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            result = op1 // op2
            return result
    except ValueError as val_err:
        raise ValueError("Ошибка ввода: {}".format(val_err))


while True:
    try:
        expression = input("Калькулятор, введите нужную операцию. (Пример 1 + 10): ")
        result = calculate(expression)
        print("Результат:", result)
    except ValueError as b:
        print(b)