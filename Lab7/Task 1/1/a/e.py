# s = v * t 
v = int(input())
t = int(input())

if v > 0:
    s = (v * t)%109
    print(s)
else:
    print(108)