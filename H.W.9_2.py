def difference(*args):
    # перевіряємо чи не передано жодного аргументу
    if not args:
        return 0
    # знаходимо макс і мін значення
    max_value = max(args)
    min_value = min(args)
    # обчислюємо різницю
    diff = max_value - min_value
    # округлюємо результат до знаків після коми
    return round(diff, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
