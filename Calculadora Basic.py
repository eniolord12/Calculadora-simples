#CALCULADORA QUE REALIZA FUNÇÂOES BASICAS COMO: ADIÇÂO, SUBTRAÇÃo, MULTIPLICAÇÃO, DIVISÃO, POTÊNCIA
#A definição de cada função - calculos de\/
#Adição, subtração, multiplicação, divisão, potência
def adição(n1,n2):
    resultado=n1+n2
    return resultado
def subtração(n1,n2):
    resultado=n1-n2
    return resultado
def multiplicação(n1,n2):
    resultado=n1*n2
    return resultado
def divisão(n1,n2):
    resultado=n1/n2
    return resultado
def potência(n1,n2):
    resultado=n1**n2
    return resultado

#Ira imprimir a frase inicial do projeto
print('Seja bem vindo ao teste da calculadora!')

#enquanto for escrito "S" ao final do processo, ele reiniciara
control = True
while(control==True):

#Função da incersão dos nº
    n1 = float(input('Insira o primeiro nº:'))
    n2 = float(input('Insira o segundo nº:'))

#Função String onde ira mostras quais opções se tem para inserir
    print('Selecione uma das operações:')
    operador = int(input('1) Adição \n2) Subtração \n3) Multiplicação \n4) Divisão \n5) Potência \nR.:'))

#Dando funcionalida ao texto acima
#Fara a ação de acordo com o numero seleciondo
    if(operador == 1):
        adição = adição(n1,n2)
        print('{} + {} ='.format(n1,n2))
        print(n1+n2)
    if(operador == 2):
        subtração = subtração(n1,n2)
        print('{} - {} ='.format(n1, n2))
        print(n1 - n2)
    if(operador == 3):
        multiplicação = multiplicação(n1,n2)
        print('{} * {} ='.format(n1, n2))
        print(n1 * n2)
    if(operador == 4):
        divisão = divisão(n1,n2)
        print('{} / {} ='.format(n1, n2))
        print(n1 / n2)
    if (operador == 5):
        potência = potência(n1, n2)
        print('{} ^ {} ='.format(n1, n2))
        print(n1 ** n2)

#Oque acontecera caso o função selecionada seja inesistente
    if(operador >5):
        print('Por favor, digite um valor entra 1 à 5, reinicie a operação.')

#Ação para reiniciar o fizalizar processo
    control2 = input('Deseja continuar? s/n \n R.:')
    if(control2.upper()=='S'):
        control = True
    else:
        control = False
