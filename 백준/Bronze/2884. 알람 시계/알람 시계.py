H, M = map(int, input().split())

if H != 0:
    if M < 45:
        H -= 1
        M = M + 60 - 45
        print(H, M)
    else:
        M -= 45
        print(H, M)
else:
    if M < 45:
        H = 23
        M = M + 60 - 45
        print(H, M)
    else:
        M -= 45
        print(H, M)