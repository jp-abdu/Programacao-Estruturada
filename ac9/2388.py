N = int(input())
distancia = 0
for i in range(N):
    tempo, velocidade = input().split()
    tempo = int(tempo)
    velocidade = int(velocidade)
    distancia += tempo * velocidade

print(distancia)