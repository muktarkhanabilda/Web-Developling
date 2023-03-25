n = int(input())
arr = list(map(int,input().split()))

num = 0
for i in range(1,n):
    if arr[i] > arr[i-1]:
        num+=1

print(num)