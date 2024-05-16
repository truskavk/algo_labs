class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

def post_order_traversal(root: BinaryTree) -> list:
    # Початок визначення функції post_order_traversal з аргументом root, який є вузлом BinaryTree, та з визначенням повертаємого типу як list.
    result = []
    # Створення списку result для зберігання значень вузлів в порядку післяпорядкового обходу.
    stack = []
    # Створення стеку stack для тимчасового зберігання вузлів дерева.
    current = root
    # Ініціалізація змінної current як корінь дерева.

    while current or stack:
        # Початок циклу, який триває доти, доки current не є None і stack не є порожнім.
        while current:
            # Початок внутрішнього циклу, який просувається вліво по дереву, додаючи праві дочірні вузли в стек.
            if current.right:
                stack.append(current.right)
                # Якщо існує правий дочірній вузол, додаємо його до стеку.
            stack.append(current)
            # Додаємо поточний вузол до стеку.
            current = current.left
            # Переходимо до лівого дочірнього вузла.

        current: BinaryTree = stack.pop()
        # Вилучаємо вузол зі стеку.

        if stack and current.right == stack[-1]:
            # Перевірка, чи є наступним вузол у стеку правий дочірній вузол.
            stack.pop()
            # Вилучаємо правий дочірній вузол зі стеку.
            stack.append(current)
            # Додаємо поточний вузол до стеку.
            current = current.right
            # Переходимо до правого дочірнього вузла.
        else:
            result.append(current.value)
            # Якщо правого дочірнього вузла немає у стеку, додаємо значення поточного вузла до результату.
            current = None
            # Встановлюємо current в None.

    return result
    # Повертаємо список result, який містить значення вузлів у порядку післяпорядкового обходу.
