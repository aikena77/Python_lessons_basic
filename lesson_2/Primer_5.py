my_str = "Python the best"
print(my_str[2:7:2])    # start = 0: stop = len: step = 1  len - это длина строки
f = my_str.split()
print("__".join(f))    # объединение символов без пробелов
print(my_str.upper())   # пищит заглавными
print(my_str.lower())  # пишит строчными
print(my_str.title())  # пишит все  буквы с заглавной
print(my_str.capitalize())  # пишит только первую букву в предложении с заглавной
print(my_str.istitle())
print(my_str.count("t"))  # пересчитывает сколько  t есть в предложении
print(my_str.replace('t', 'TTT'))  # заменяет буквы
print(my_str.index('t'))  # показывает первого вхождения Т
print(my_str.strip('P')) # обрезает букву с обеих сторон
