# Problem: https://www.hackerrank.com/challenges/py-set-union

ne = int(input())
english = set(input().split(" "))
nf = int(input())
french = set(input().split(" "))

print(len(english.union(french)))
