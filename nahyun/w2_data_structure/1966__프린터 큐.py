def print_result(N, M):
    N = int(N); M = int(M)
    mList = list(map(int, input().split()))
    sequence = 0
    max = find_largest(mList)

    while (1):
        if (mList[0] < max): # 중요도가 높은 애가 있을 경우
            if (M == 0):
                M += len(mList)
            mList.append(mList[0])
            mList.pop(0)
        else: # 빠져나갈 애가 있을 경우
            mList.pop(0)
            sequence += 1
            if (M == 0):
                print(sequence)
                break
        M -= 1
        max = find_largest(mList)
    mList = []

def find_largest(mList):
    max = mList[0]
    for i in mList:
        if i > max:
            max = i
    return max


# 테스트 케이스의 수
num = int(input())
for i in range (num):
    # N: 문서의 개수, M: 순서가 궁금한 문서가 현재 Queue의 몇 번째에 위치하는지
    N, M = input().split()
    print_result(N, M)