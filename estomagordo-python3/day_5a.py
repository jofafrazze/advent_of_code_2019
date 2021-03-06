import re

from heapq import heappop, heappush
from collections import Counter, defaultdict


def solve(d, inp):
    p = 0

    while p < len(d):
        a = -1 if p > len(d) - 2 else d[p + 1] if ((d[p] % 1000) // 100) == 1 else d[d[p + 1]]
        b = -1 if p > len(d) - 3 else d[p + 2] if ((d[p] % 10000) // 1000) == 1 else -1 if d[p + 2] >= len(d) else d[d[p + 2]]

        if d[p] % 100 == 1:
            d[d[p + 3]] = a + b
            p += 4
        elif d[p] % 100 == 2:
            d[d[p + 3]] = a * b
            p += 4
        elif d[p] % 100 == 3:
            d[d[p + 1]] = inp
            p += 2
        elif d[p] % 100 == 4:
            if a != 0:
                return a
            p += 2


def read_and_solve():
    with open('input_5.txt') as f:
        data = list(map(int, f.readline().split(',')))
        return solve(data, 1)

if __name__ == '__main__':
    print(read_and_solve())