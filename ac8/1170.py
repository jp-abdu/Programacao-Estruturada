N = int(input())

for _ in range(N):

    C = float(input())
    resultado = 0

    while (C > 1.0):
        resultado += 1
        C /= 2

    print(f'{resultado} dias')