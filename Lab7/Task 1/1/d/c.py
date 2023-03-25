n = int(input())
arr = list(map(int,input().split()))
num = 0

for i in range(n):
    if arr[i] > 0:
        num+=1

print(num)