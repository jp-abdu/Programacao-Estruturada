#Exercício 1- Hello World!
print("Hello World!")

print("-"*30)

#Exercício 2- Extremamente Básico
def extremamente_basico():
    a=int(input())
    b=int(input())
    X=a+b
    print(f"X = {X}")

extremamente_basico()

print("-"*30)

#Exercício 3- Calculo Simples
def calculo_simples():
    dados1 = input()
    dados2 = input()
    dados1 = dados1.split(" ")
    dados2 = dados2.split(" ")
    preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
    print(f"VALOR A PAGAR: R$ {preco:.2f}")

calculo_simples()

print("-"*30)

#Exercício 4- O Maior
def O_Maior():
    a, b, c = input().split()
    a= int(a)
    b= int(b)
    c= int(c)
           
    maiorAB= (a+b+abs(a-b))/2
    maiorABC = (maiorAB + c + abs(maiorAB-c))/2

    print(f'{maiorABC:.0f} eh o maior')

O_Maior()

print("-"*30)

#Exercício 5- Distância entre dois pontos
def distancia():
    x1,y1=input().split(" ")
    x2,y2=input().split(" ")
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)  
    result = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  
    print(f"{result:.4f}")

distancia()

print("-"*30)