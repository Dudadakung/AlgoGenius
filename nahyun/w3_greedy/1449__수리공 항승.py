def find_result(N, L, fList):
    count = 1
    start_pos = fList[0]

    for i in range (len(fList)):
        if (fList[i] < start_pos + L):
            continue
        else:
            start_pos = fList[i]
            count += 1
    print(count)

N, L = input().split()
N = int(N); L = int(L)
mList = list(map(int, input().split()))
mList.sort()
find_result(N, L, mList)