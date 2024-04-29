x = int(input())
frequencia = [0 for _ in range(2001)]

for _ in range(x):

    y = int(input())
    frequencia[y] += 1

for i in range(1, 2001):

    if(frequencia[i] > 0):
        print(f"{i} aparece {frequencia[i]} vez(es)")