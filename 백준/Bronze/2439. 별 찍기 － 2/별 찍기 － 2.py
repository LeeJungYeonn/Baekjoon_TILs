n = int(input())

for i in range (1, n+1):
    print(" " * (n-i) + "*" * i)

# print(" " * (n-i) , "*" * i)
# -> 쉼표에 의해서 출력하는 값들 사이에 구분자가 들어가기 때문에 공백이 생긴다!
# 다른 방법) print(" " * (n-i) , "*" * i, sep="")