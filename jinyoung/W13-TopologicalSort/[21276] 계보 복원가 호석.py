from sys import stdin
from collections import deque


N = int(stdin.readline())

name = list(map(str, stdin.readline().split()))
name.sort()
name_dict = dict()
for i in range(N):
    name_dict.update({name[i]:i})

person_after = [[] for _ in range(N)]
person_before_cnt = [0 for _ in range(N)]
person_childs = [[] for _ in range(N)]
ancestor = []

M = int(stdin.readline())
for i in range(M):
    child, parent = map(str, stdin.readline().split())
    person_before_cnt[name_dict.get(child)] += 1
    person_after[name_dict.get(parent)].append(name_dict.get(child))

for i in range(N):
    person_after[i].sort()

que = deque()

for i in range(N):
    if person_before_cnt[i] == 0:
        que.append(i)
        ancestor.append(name[i])

while que:
    person = que.popleft()
    for child in person_after[person]:
        person_before_cnt[child] -= 1
        if person_before_cnt[child] == 0:
            que.append(child)
            person_childs[person].append(name[child])

print(len(ancestor))
print(*ancestor)

for person in name:
    print(person, len(person_childs[name_dict.get(person)]), end=" ")
    print(*person_childs[name_dict.get(person)])
        
        
