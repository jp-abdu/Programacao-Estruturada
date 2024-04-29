#Tive que pesquisar essa, não consegui fazer, acho que entendi mas ainda estou meio confuso

import math


def Crivo(x):
    C = [True for _ in range(x)]
    primos = []

    C[1] = False
    primos.append(2)

    for i in range(4, x, 2):
        C[i] = False

    for i in range(3, x, 2):
        if(C[i]):
            primos.append(i)

            for j in range(i * 3, x, 2 * i):
                C[j] = False

    return primos


def e_primo(primos, x):
    limite = math.ceil(math.sqrt(x))

    for primo in primos:
        if(primo > limite):
            return True
        elif(x % primo == 0):
            return (x == primo)

    return True


primos = Crivo(65536)

Y = int(input())

for _ in range(Y):
    X = int(input())

    print('Prime' if e_primo(primos, X) else 'Not Prime')

