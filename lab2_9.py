numbers_input = input("Введите несколько чисел, разделенных пробелом: ")
numbers = list(map(float, numbers_input.split()))
max_number = max(numbers)
print(f"Максимальное число в списке {numbers} равно {max_number}")
