def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)


Numero = int(input())

for _ in range(Numero):
    Y1, Y2 = [int(x) for x in input().strip().split(' ')]
    print(MDC(Y1, Y2))
