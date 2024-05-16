def has_cycle(graph):
    # Початок визначення функції has_cycle з аргументом graph, що є представленням графа.
    visited = set()
    # Створення множини visited для відстеження відвіданих вершин графа.
    stack = []
    # Створення стеку stack для відстеження шляху в графі.

    for vertex in graph:
        # Ітерація по вершинах графа.
        if vertex not in visited:
            # Перевірка, чи вершина не відвідана.
            if dfs(graph, vertex, visited, stack, parent=None):
                # Виклик функції dfs для перевірки наявності циклу в графі.
                write_file(True)
                # Запис результату у файл як True.
                return True

    write_file(False)
    # Якщо цикл не знайдено, запис результату у файл як False.
    return False

def dfs(graph: dict, current, visited: set, stack: list, parent):
    # Початок визначення функції dfs для пошуку циклу у графі.
    visited.add(current)
    # Додаємо поточну вершину до відвіданих.

    stack.append(current)
    # Додаємо поточну вершину до стеку.

    if current in graph.keys():
        # Перевіряємо, чи існує поточна вершина у графі.
        for neighbor in graph[current]:
            # Ітеруємося по всім сусіднім вершинам поточної вершини.
            if neighbor not in visited:
                # Перевіряємо, чи сусідня вершина не відвідана.
                if dfs(graph, neighbor, visited, stack, current):
                    # Рекурсивно викликаємо dfs для сусідньої вершини.
                    return True
            elif neighbor != parent:
                # Якщо сусідня вершина вже відвідана і не є батьківською, це означає наявність циклу.
                return True

    stack.pop()
    # Видаляємо поточну вершину зі стеку.
    return False

def read_file(filename="src/input.txt"):
    # Визначення функції для читання даних з файлу.
    with open(filename, "r") as file:
        output = {}
        line = file.readline()
        while line:
            a, b = line.split(": ")
            a = int(a)
            b = list(map(int, b.split(", ")))

            output[a] = b

            line = file.readline()
        return output

def write_file(result, filename="src/output.txt"):
    # Визначення функції для запису результату у файл.
    with open(filename, "w") as file:
        file.write(str(result))


if __name__ == "__main__":
    # Виконання коду, якщо файл запускається напряму.
    print(has_cycle(read_file()))
    # Виклик функції has_cycle для графа, зчитаного з файлу, і вивід результату.
