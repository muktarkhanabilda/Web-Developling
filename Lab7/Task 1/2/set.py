def average(arr):
    # your code goes here
    arrlen = set(arr)
    avg = sum(arrlen)/len(arrlen)
    return round(avg,3)
    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)