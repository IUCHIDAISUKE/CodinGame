import sys
import math

l = int(input())
h = int(input())
t = input()
row = [input() for i in range(h)]
answer = []

for c in t:
    if('A' <= c <= 'Z'):
        answer.append((ord(c) - ord('A')) * 4)
    elif ('a' <= c <= 'z'):
        answer.append((ord(c) - ord('a')) * 4)
    else:
        answer.append(26 * 4)
for i in range(h):
    for k in answer:
        print(row[i][k:k+l], end='')
    print()
