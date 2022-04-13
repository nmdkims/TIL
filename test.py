import sys

input =sys.stdin.readline

N = int(input())

num =[0]*10001

for _ in range(N):
    temp = int(input())
    num[temp] += 1

for i in range(10001):
    if num[i] !=0:
        for j in range(num[i]):
            print(i)