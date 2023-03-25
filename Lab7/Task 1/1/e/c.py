def xor(x,y):
    return (x or y) and not (x and y)

print(xor(0, 1)) 
print(xor(1, 1))   
print(xor(0, 0)) 
