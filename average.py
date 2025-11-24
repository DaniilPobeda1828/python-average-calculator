"""
Модуль для вычисления среднего арифметического значения списка чисел.
"""

def calculate_average(numbers: list[float]) -> float | None:
    """
    Вычисляет среднее арифметическое значение элементов в списке.

    Args:
        numbers (list[float]): Список чисел для расчета.

    Returns:
        float | None: Среднее значение списка. Возвращает None, если список пуст.
    """
    # Проверка на пустой список в начале функции для раннего возврата.
    # Это улучшает читаемость и следует принципу "Guard Clause".
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


if __name__ == "__main__":
    # Пример использования и простые тесты.
    # Вынесен в блок, который выполняется только при прямом запуске скрипта.
    
    test_data = [10, 20, 30, 40]
    expected_result = 25.0
    
    result = calculate_average(test_data)
    
    # Простая проверка для демонстрации
    if result == expected_result:
        print(f"✅ Тест пройден: Среднее значение {test_data} равно {result}")
    else:
        print(f"❌ Тест не пройден: Ожидалось {expected_result}, получено {result}")

    # Тест с пустым списком
    empty_list_result = calculate_average([])
    if empty_list_result is None:
        print("✅ Тест с пустым списком пройден")
    else:
        print(f"❌ Тест с пустым списком не пройден: Ожидалось None, получено {empty_list_result}")
