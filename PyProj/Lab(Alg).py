#1

numbers = [int(x) for x in input().split()]
min_positive = 1001

for num in numbers:
    if num > 0 and num < min_positive:
        min_positive = num

print(min_positive)

#2
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

count = 0
row, col = 0, m - 1

while row < n and col >= 0:
    if matrix[row][col] < 0:
        count += (n - row)
        col -= 1
    else:
        row += 1

print(count)

#3
n = int(input())
matrix = [input().strip() for _ in range(n)]
if n == 0:
    print(0)
    exit()

m = len(matrix[0])
count = 0

for j in range(m):
    is_ordered = True
    for i in range(n - 1):
        if matrix[i][j] > matrix[i + 1][j]:
            is_ordered = False
            break
    if not is_ordered:
        count += 1

print(count)
