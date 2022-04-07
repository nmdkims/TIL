import sys

N, M = map(int, sys.stdin.readline().split())
matrixA = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().split())
matrixB = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for n in range(N):
    for k in range(K):
        tmp = 0
        for m in range(M):
            tmp += matrixA[n][m] * matrixB[m][k]

        sys.stdout.write(str(tmp) + " ")
    sys.stdout.write("\n")
