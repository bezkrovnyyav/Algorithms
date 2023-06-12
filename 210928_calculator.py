# Задача на программирование: калькулятор
# У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
# заменить x на 2x, 3x или x+1. По данному целому числу 1 ≤ n ≤ 10^5 определите минимальное число
# операций k, необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.


n = int(input())

res = [n]
mtx = [0] * (n + 1)

for i in range(1, n + 1):
    m = mtx[i - 1] + 1
    if i % 2 == 0:
        m = min(m, mtx[i // 2] + 1)
    if i % 3 == 0:
        m = min(m, mtx[i // 3] + 1)
    mtx[i] = m

while n > 1:
    if mtx[n] == mtx[n - 1] + 1:
        n -= 1
    elif n % 2 == 0 and mtx[n] == mtx[n // 2] + 1:
        n //= 2
    else:
        n //= 3
    res.append(n)

print(len(res) - 1)
print(*res[::-1])

