# Задача на программирование: очередь с приоритетами. Первая строка входа содержит число
# операций 1 ≤ n ≤ 10^5. Каждая из последующих n строк задают операцию одного из следующих
# двух типов:
# Insert x, где 0 ≤ x ≤ 10^9  — целое число;
# ExtractMax.

# Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное
# число и выводит его.

# Sample Input:
# 6

# Insert 200
# Insert 10
# ExtractMax
# Insert 5
# Insert 500
# ExtractMax

# Sample Output:
# 200
# 500

import heapq
heap = []
for line in range(int(input())):
    line = input()
    if line.startswith('Insert'):
        func, num = line.split()
        heapq.heappush(heap, int(num) * -1)
    else:
        print(-heapq.heappop(heap))

