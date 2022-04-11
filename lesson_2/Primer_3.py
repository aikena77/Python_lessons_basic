i = 0
while True: # бесконечный цикл
    i += 1
    if i >= 10:
        break # выход из цикла
    if i % 2 == 0:
        continue # переход на следующую итерацию
    print(i)

