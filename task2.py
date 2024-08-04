def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                line = line.strip()
                parts = line.split(',')
                if len(parts) == 3:
                    try:
                        id = parts[0]
                        name = parts[1]
                        age = int(parts[2])
                        cats.append({
                            "id": id,
                            "name": name,
                            "age": age
                        })
                    except ValueError:
                        print(f"Помилка перетворення віку рядка: {line}")
                else:
                    print(f"Неправильний формат рядка: {line}")
            return cats
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
        return None


cats = get_cats_info("cats.txt")
print(cats)