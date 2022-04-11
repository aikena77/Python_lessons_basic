age = int(input("Введите свой возвраст? "))
country = "Kazaxstan"
if age > 16 and country == "Kazaxstan":
    print("HELLO")
    name = input("Как вас зовут? ")
    if name == "admin":
        print("Hi, "  + name )
    else:
        print("Goodbuy")
else:
    print("SSORY")
print("Ваше имя %s, Ваш возвраст %d " % (name, age)) # %s форматирование строки   %d - форматирование чисел
print("Ваше имя {}, Ваш возвраст {} " .format (name, age)) # современный способ
print(f"Ваше имя {name}, Ваш возвраст {age}")  # еще лучше способ форматирования