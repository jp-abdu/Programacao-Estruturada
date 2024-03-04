#Exercício 1:

'''
Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve ler os parâmetros a, b e c da equação
e deve calcular as raízes pela fórmula de Bhaskara.
'''

a= float(input('Informe um valor de a: '))
b= float(input('Informe um valor de b: '))
c= float(input('Informe um valor de c: '))

delta= (b**2) - (4*a*c) #Calcular delta

raiz1= (-b + delta**(0.5)) / (2*a)
raiz2= (-b - delta**(0.5)) / (2*a)

print(f'A primeira raiz da equação vale:', raiz1)
print(f'A segunda raiz da equação vale:', raiz2)

print('-'*30)

#Exercício 2
ano= int(input('Informe o ano: '))
ano_bissexto= ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0)) 
#Divisível por 4, e exceção do 400
print(ano_bissexto)