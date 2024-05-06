C, P, F = [int(x) for x in input().strip().split(' ')]
if P >= C * F:
    print('S')
else:
    print('N')