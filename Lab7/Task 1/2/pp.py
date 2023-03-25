from itertools import permutations

s, r = input().split()
perms = permutations(sorted(s), int(r))

for p in perms:
    print(''.join(p))
