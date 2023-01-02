# Problem: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

hashMap = {}
for i in range(4):
    s = input()
    hashMap[s] = hashMap.get(s, 0) + 1
    
print(len(hashMap.values()))

for i in hashMap.values():
    print(i, end=" ")
    
print(hashMap)
