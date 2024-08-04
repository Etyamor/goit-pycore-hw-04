def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total, count = 0, 0
            for line in file:
                line = line.strip()
                parts = line.split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Помилка перетворення зарплати в числовий формат для рядка: {line}")
                else:
                    print(f"Неправильний формат рядка: {line}")

            if count == 0:
                return None, None

            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
        return None, None


total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
