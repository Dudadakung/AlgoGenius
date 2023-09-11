global cnt
global result

cnt = 0; result = -1

def merge_sort(A, p, r): # A[p..r]을 오름차순 정렬한다.
    if (p < r): 
        q = (p + r) // 2         # q는 p, r의 중간 지점
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    global cnt
    global result
    i = p; j = q + 1; t = 0
    tmp = [0] * (r - p + 1)
    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp[t] = A[i] # tmp[t] <- A[i]; t++; i++;
            t += 1; i += 1
        else:
            tmp[t] = A[j]; # tmp[t] <- A[j]; t++; j++;
            t += 1; j += 1
    while (i <= q):  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        t += 1; i += 1
    while (j <= r):  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        t += 1; j += 1
    i = p; t = 0
    while (i <= r):  # 결과를 A[p..r]에 저장
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            result = A[i]
        t += 1; i += 1

def find_result(A, p, r, k):
    merge_sort(A, p, r)
    return(result)

# 입력 받기
N, K = input().split()
N = int(N); K = int(K)
mList = list(map(int, input().split()))
# K번째로 저장되는 수 찾기
print(find_result(mList, 0, N - 1, K))