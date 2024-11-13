numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Список
primes = [] # Пустой список 1
not_primes = [] # Пустой список 2
for num in numbers: # Цикл перебора номеров
    if num == 1: # Один делится на один, скипаем
        continue
    is_prime = True # Флаг для определения простоты числа
    for i in range(2, int(num ** 0.5) + 1): # Делим от 2 до num+1, range игнорирует крайнюю цифру, поэтому +1
        if num % i == 0: # Делится ли num на i и равен ли остаток 0
            is_prime = False # Флаг меняется, если число не простое
            break # Прерывание цикла, дальше нет смысла
    if is_prime: # Если простое, добавляем в один список
        primes.append(num)
    else: # Если нет, во второй список
        not_primes.append(num)
print("Primes:", primes)
print("Not Primes:", not_primes)