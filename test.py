import sys

sys.stdin = open("input.txt", 'r')


def get_best_mas_sal(n):
    ma = [list(map(int, input().split())) for i in range(n)]
    ma.sort(reverse=True, key=lambda x: (x[0] / x[1], -x[1]))

    return ma[0][1]


for j in range(int(input())):
    print(get_best_mas_sal(int(input())))