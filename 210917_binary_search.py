# Задача на программирование: двоичный поиск. В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив
# A[1 ... n] из n различных натуральных чисел, не превышающих 10^9, в порядке возрастания, во второй
# — целое число 1 ≤ k ≤ 10^5 и k натуральных чисел b_1, b_k, не превышающих 10^9. Для каждого i от 1
# до k необходимо вывести индекс 1 ≤ j ≤ n, для которого A[j]=b_i, или -1, если такого j нет.

# Sample Input:
# 5 1 5 8 12 13
# 5 8 1 23 1 11
#
# Sample Output:
# 3 1 -1 1 -1

n, *arr = list(map(int, input().split()))
n, *nums = list(map(int, input().split()))

import bisect
def bin_search(arr, num):
    low = bisect.bisect_left(arr, num)
    if low < len(arr) and arr[low] == num:
        return low + 1
    return -1

print(*[bin_search(arr, x) for x in nums])
