m, n = map(int, input().split())

A = []
B = []

# Input first matrix
for _ in range(m):
    A.append(list(map(int, input().split())))

# Input second matrix
for _ in range(m):
    B.append(list(map(int, input().split())))

# Add and print result
for i in range(m):
    for j in range(n):
        print(A[i][j] + B[i][j], end=" ")
    print()
