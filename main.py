def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Присваиваем b значение остатка от деления a на b
    return a

# Пример использования
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

gcd = euclid_gcd(num1, num2)
print(f"НОД чисел {num1} и {num2} = {gcd}")
