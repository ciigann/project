print("Задание 1")
a = int(input('введите первое число: '))
b = int(input('введите второе число: '))

print("Cумма", a, "и", b, "равна:", a + b)
print("Разность", a, "и", b, "равна:", a - b)
print("Произведение", a, "и", b, "равно", a * b)
print("Среднее арифметическоe", a, "и", str(b) + " равно:", (a + b)/2)

if a < 0:
    a = a * -1
if b < 0:
    b = b * -1
if a > b:
    c = a - b
else:
    c = b - a
print("Разность максимального и минимального по модулю равна:", c)



print("\nЗадание 2")
print("Назовите своё имя")
name = input()
print("Назовите свой возраст")
age = input()
print("Назовите свою страну и город проживания")
contry, city = map(str, input().split())
print("Уважаемый " + name + "!\nНа сегодняшний день Вы проживаете в стране " + contry + ",\nв городе " + city + ",\nи вы родились в " + str(2023 - int(age)) + " году.")
