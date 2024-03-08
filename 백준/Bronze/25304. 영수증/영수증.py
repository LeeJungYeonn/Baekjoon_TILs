total = int(input())
n = int(input())
a = 0
b = 0
calc = 0

for i in range(n):
    a, b = map(int, input().split())
    calc += a * b

if calc == total:
    print("Yes")

else:
    print("No")