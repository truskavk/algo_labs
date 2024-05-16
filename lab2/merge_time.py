def merge_time(time_ranges): # Початок визначення функції merge_time з аргументом time_ranges
    if len(time_ranges) == 0: # Перевірка, чи список time_ranges порожній; якщо так, повертається порожній список
        return []

    sorted_ranges = sorted(time_ranges, key=lambda x: x[0]) # Сортування списку time_ranges за першим елементом (початком інтервалу)

    merged_ranges = [sorted_ranges[0]] # Створення списку merged_ranges, в якому перший елемент - перший інтервал після сортування

    for current_range in sorted_ranges[1:]: # Ітерація по списку від другого елемента до останнього
        last_merged_range = merged_ranges[-1] # Отримання останнього об'єднаного інтервалу

        if current_range[0] <= last_merged_range[1]: 
            # Перевірка, чи початок поточного інтервалу менший або рівний кінцю останнього об'єднаного інтервалу
            last_merged_range = (last_merged_range[0], max(last_merged_range[1], current_range[1])) 
            # Об'єднання поточного інтервалу з останнім об'єднаним
            merged_ranges[-1] = last_merged_range 
            # Оновлення останнього об'єднаного інтервалу
        else:
            merged_ranges.append(current_range)
            # Якщо поточний інтервал не перетинається з останнім об'єднаним, то додаємо його до списку об'єднаних інтервалів

    return merged_ranges  # Повертає список об'єднаних інтервалів
