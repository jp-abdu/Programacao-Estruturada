#Exercicio 1
def determina_tipo_triangulo(a, b, c):
    # Verifica se os lados formam um triângulo
    if a + b > c and a + c > b and b + c > a:
        #Verifica o tipo do triângulo:
        if a == b == c:
            return "É Equilátero"
        
        elif a == b or a == c or b == c:
            return "É Isósceles"
        
        else:
            return "É Escaleno"
    else:
        return "Não é um triângulo"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

testa_triangulo()



print('-'*30)



#Exercício 2

def dia_semana(int):
    inteiro=int #int(input('Informe um número: '))
    if inteiro == 1:
        return "Domingo"
    if inteiro == 2:
        return "Segunda-feira"
    if inteiro == 3:
        return "Terça-feira"
    if inteiro == 4:
        return "Quarta-feira"
    if inteiro == 5:
        return "Quinta-feira"
    if inteiro == 6:
        return "Sexta-feira"
    if inteiro == 7:
        return "Sabado"
    else:
        return ""
    
def testa_dia_semana():
    print(dia_semana(int=2)) # segunda-feira
    print(dia_semana(int=6)) # sexta-feira
    print(dia_semana(int=7)) # sábado
    print(dia_semana(int=9)) # string vazia5
    
testa_dia_semana()


print('-'*30)


#Exercício 3

def soma(numero1, numero2):
    return numero1+numero2

def subtracao(numero1, numero2):
    return numero1-numero2


def multiplicacao(numero1, numero2):
    return numero1*numero2


def divisao(numero1, numero2):
    if numero2 == 0:
        return 'Operação Inválida'
    else:
        return numero1/numero2

def calculadora_simples():
    numero1= float(input('Informe um número: '))
    numero2= float(input('Informe outro número: '))
    operacao= input('Digite a operação( +, -, *, /): ')

    if operacao == '+':
        print(f'O Resultado é: {soma(numero1, numero2)}')
    elif operacao == '-':
        print(f'O Resultado é: {subtracao(numero1, numero2)}')
    elif operacao == '*':
        print(f'O Resultado é: {multiplicacao(numero1, numero2)}')
    elif operacao == '/':
        print(f'O Resultado é: {divisao(numero1, numero2)}')
    elif operacao != '+' or '-' or '*' or '/':
        print('Operação Inválida')

calculadora_simples()
