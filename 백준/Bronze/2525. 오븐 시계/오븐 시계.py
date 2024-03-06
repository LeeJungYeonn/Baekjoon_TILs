hr, min = map(int, input().split())
cooking_time = int(input())         # 0 ~ 1000분 사이

hr += (cooking_time // 60)
min += (cooking_time % 60)

if min >= 60:
    hr += 1
    min -= 60
if hr >= 24:
    hr -= 24

print(hr, min)