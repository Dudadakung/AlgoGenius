N = input()

# 자릿수
digits = len(N)

# 왼쪽과 오른쪽을 비교할 변수
sum = 0

for i in range (int(digits/2)):
    # 왼쪽이면 더하고, 오른쪽아면 뺀다
    sum += int(N[i])
    sum -= int(N[digits - i - 1])

if (sum == 0):
    print("LUCKY")
else:
    print("READY")
