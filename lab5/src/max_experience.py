def max_experience(graph, level=0, position=0, visited=None):
    # Початок визначення функції max_experience з аргументами graph, level, position та visited (зі значенням за замовчуванням None).
    if level == len(graph):
        # Перевірка, чи рівень дорівнює довжині графу (граф повністю оброблений).
        return 0
        # Якщо так, повертаємо 0, оскільки немає додаткового досвіду.

    if not visited:
        # Перевірка, чи відвідані вершини не ініціалізовані.
        visited = set()
        # Якщо так, ініціалізуємо visited як порожню множину.

    if (level, position) not in visited:
        # Перевірка, чи поточний рівень та позиція не були відвідані раніше.
        visited.add((level, position))
        # Додаємо поточний рівень та позицію до відвіданих.

        current_experience = graph[level][position]
        # Отримуємо досвід на поточному рівні та позиції.
        left_experience = max_experience(graph, level + 1, position, visited)
        # Рекурсивний виклик функції для лівого наступного рівня.
        right_experience = max_experience(graph, level + 1, position + 1, visited)
        # Рекурсивний виклик функції для правого наступного рівня.

        return current_experience + max(left_experience, right_experience)
        # Повертаємо суму поточного досвіду та максимуму досвіду з лівого та правого наступних рівнів.
    else:
        return 0
        # Якщо поточний рівень та позиція були відвідані раніше, повертаємо 0.

if __name__ == "__main__":
    # Початок виконання коду, якщо файл запускається напряму.
    with open("src/career.in", "r") as file:
        L = int(file.readline())
        experience = [list(map(int, file.readline().split())) for _ in range(L)]
        # Зчитуємо дані з файлу в змінну experience.

    result = max_experience(experience)
    # Викликаємо функцію для знаходження максимального досвіду.

    with open("src/career.out", "w") as file:
        file.write(str(result))
        # Записуємо результат у вихідний файл.