# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation

ne = int(input())
english = set(list(map(int, input().split(' '))))
nf = int(input())
french = set(list(map(int, input().split(' '))))

print(len(english.difference(french)))
