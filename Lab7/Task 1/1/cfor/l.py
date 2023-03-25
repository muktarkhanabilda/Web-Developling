binary = input()

decimal = 0

for i in range(len(binary)):
    decimal += int(binary[i])* 2 ** (len(binary)- 1 - i)

print(decimal)