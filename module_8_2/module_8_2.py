def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            print('Некорректные данные')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            print('В numbers записан некорректный тип данных')
            return None

        total_sum, incorrect_count = personal_sum(numbers)

        valid_count = len(numbers) - incorrect_count
        if valid_count == 0:
            return 0

        return total_sum / valid_count

    except ZeroDivisionError:
        print('Деление на ноль при вычислении среднего')
        return 0

    except Exception as e:
        print(f'Произошла непредвиденная ошибка: {e}')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
