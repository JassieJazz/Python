def calculate(res):
        components = res.split()
        if len(components) != 3:
            raise ValueError("Неверный формат ввода. Попробуйте например: '2 + 3'")
        opperand1, operator, opperand2 = components
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Недопустимый оператор: должен быть одним из '+', '-', '*', '/'")
        if not (opperand2.isdigit() and opperand1.isdigit()):
            raise ValueError("Операнды должны быть числами")
        a = int(a)
        b = int(b)
        if not (1 <= opperand1 <= 10 and 1 <= opperand2 <= 10):
            raise ValueError("Операнды должны быть целыми числами от 1 до 10")


        if operator == '+':
            return opperand1 + opperand2
        elif operator == '-':
            return opperand1 - opperand2
        elif operator == '*':
            return opperand1 * opperand2
        elif operator == '/':
            result = opperand1 // opperand2 
            return result


        res = input("Калькулятор для математической операции - два операнда и один оператор (+, -, /, *)\nВведите выражение (например, 2 + 3): ")
        result = calculate(res)
        print("Результат:", result)