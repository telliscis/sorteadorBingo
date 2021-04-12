from random import randint

lista = []
i = 1

def gerarNumero():
    numero = randint(1,75)
    if numero <=15:
        if numero < 10:
            novoNum = "B0" + str(numero)
        else:
            novoNum = "B" + str(numero)

    if numero >15 and numero <=30:
        novoNum = "I" + str(numero)
   
    if numero >30 and numero <=45:
        novoNum = "N" + str(numero)

    if numero > 45 and numero <=60:
        novoNum = "G" + str(numero)

    if numero >60:
        novoNum = "O" + str(numero)
    
    if novoNum not in lista:
            lista.append(novoNum)
            print(novoNum)
    else:
        gerarNumero()
    
def imprimirLista():
    lista.sort()
    print("Numeros sorteados: ",lista)
    print('Total de numeros sorteados: ',len(lista))
    
print("Bem vindo ao sorteador de numeros para bingo")

while i > 0 and len(lista) < 75:
    escolha = input('Digite "1" para novo numero, "2" para ver numeros sorteados ou "0" para sair: ')
    if escolha == '1':
        gerarNumero()
    elif escolha == '2':
        imprimirLista()
    elif escolha == '0':
        i = 0
    else:
        print("Opção inválida!!")
        
print('Fim de Jogo !!!!')
imprimirLista()

