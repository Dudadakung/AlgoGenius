N = int(input())
mList = []
max_count = 0
max_word = ""

for i in range (N):
    mList.append(input())
mList.sort()
for a in mList:
    if (mList.count(a) > max_count):
        max_count = mList.count(a)
        max_word = a
print(max_word)