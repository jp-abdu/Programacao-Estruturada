#Exercício 1:
'''
Desenvolva duas funções em Python:

eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0, supondo as 
raízes sempre reais;

bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
'''

def eq_seg_grau(a, b, c):
    a= float(input('Informe um valor de a: '))
    b= float(input('Informe um valor de b: '))
    c= float(input('Informe um valor de c: '))
    delta= (b**2) - (4*a*c)
    raiz1= (-b + delta**(0.5)) / (2*a)
    raiz2= (-b - delta**(0.5)) / (2*a)
    print('A primeira raiz da equação vale:', raiz1)
    print('A segunda raiz da equação vale:', raiz2)
    print('-'*30)

eq_seg_grau(a=(), b=(), c=())


def bissexto(ano):
    ano= int(input('Informe o ano: '))
    ano_bissexto= ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0))
#Divisível por 4, e exceção do 400
    print(ano_bissexto)

bissexto(ano=())


#Exercicio 2:
'''
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe dois parâmetros posicionais reais, valor_hora e num_horas, 
que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente. Além disso, a função tem um 
parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275. A função retorna o salário líquido de um 
funcionário, calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado.
'''

def calcula_salario(valor_hora, num_horas, irpf):
    valor_hora = float(input('Informe seu salario por hora: '))
    num_horas = float(input('Informe suas horas mensais: '))
    salario_bruto = valor_hora * num_horas
    salario_liquido = salario_bruto - salario_bruto * irpf
    print(salario_liquido)

calcula_salario(valor_hora=(), num_horas=(), irpf=0.275)
