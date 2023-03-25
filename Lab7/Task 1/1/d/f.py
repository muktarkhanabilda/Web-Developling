n = int(input())
arr = list(map(int,input().split()))
num = 0

for i in range(n):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        num+=1

print(num)