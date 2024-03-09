import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except ValueError: 
        break

# 예외(exception) : 코드를 실행하는 중에 발생한 에러
# 예외가 발생했을 때도 스크립트 실행을 중단하지 않게 하는 예외 처리 방법

# try:
#     실행할 코드
# except (예외) (as 변수):
#     예외 발생 시 처리할 코드
# -> [as 변수] 지정 시 에러 메시지 받아올 수 있다 (print(변수)하면 메시지 출력 가능)

# try 구문 내부에서 에러 발생 시 except 구문으로 넘어감. try 구문 내부에서 에러 발생한 이후 코드들은 실행되지 않는다.