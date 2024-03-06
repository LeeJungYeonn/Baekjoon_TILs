A,B=map(int,input().split()) # 입력; A와 B는 "공백 한 칸으로 구분"되어져 있다.

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
