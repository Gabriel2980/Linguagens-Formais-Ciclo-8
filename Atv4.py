import math
import time

def criarADF(estados):

    def ADF(simboloNovo):
        estadosPossiveis = []
        estadosFuturos = 0
        estadosPossiveis.append(estados[2][0])
        for simbolo in simboloNovo:
            copiaEstadosPossiveis = estadosPossiveis
            for estadoAtual in copiaEstadosPossiveis:
                print("Estado autal:", estadoAtual)
                print("Simbolo:", simbolo)

                for i in range(len(estados[0])):
                    print("Estado Teste i:", estados[0][i])
                    if(estados[0][i] == estadoAtual):
                        break
                for j in range(len(estados[1])):
                    print("Estado Teste j:", estados[1][j])
                    if(estados[1][j] == simbolo):
                        break
                print("i: %d J: %d" %(i, j))
                
                for verificar in estados[i+4][j+1]:
                    if(verificar == ','):
                        estadosFuturos += 1
                print(estadosFuturos)
                time.sleep(3)
                for todosCasos in range(estadosFuturos+1):
                    if(estados[i+4][j+1] != 'vazio'):
                        print(estados[i+4][j+1])
                        print(i)
                        print(j)
                        estadosPossiveis.append(estados[i+4][j+1][todosCasos*3:2+todosCasos*3])
                print(estadosPossiveis)
                estadosPossiveis.pop(0)
                print(estadosPossiveis)

            time.sleep(3)
        print("Aqui")
        resultado = 'rejeita'
        for estadoAtual in estadosPossiveis:
            if(estadoAtual in estados[2]):
                resultado = 'aceita'
        return resultado
    return ADF

def adicionarEstado(novaInformacao, etapaAtualIndex):
    if(len(estadosADF) <= etapaAtualIndex):
        estadosADF.append([])
    estadosADF[etapaAtualIndex].append(novaInformacao)
    return estadosADF

#criando os índex para as etapas de criação da ADF 
etapaAtualIndex = 0

novaInformacao = None

#criando matriz para guardar os estados, estados de aceitação, alfabeto e transferência
estadosADF = []

#criando todas etapas da ADF
etapaDeCriacaoDaADF = ['CriandoEstados', 'CriandoAlfabeto', 'EstadoInicial', 'EstadosDeAceitacao', 'Transferencia']

while(etapaAtualIndex <= len(etapaDeCriacaoDaADF)-1+(len(estadosADF[0]) if len(estadosADF) > 0 else 0)):
    #Guardando todo o input do site para criar o automato  
    automato = input()
    for letraNova in automato: 

        #adiciona uma letra na string novaInformacao até encontrar um espaço ou \n
        if(letraNova != ' '):
            if(novaInformacao == None):
                novaInformacao = letraNova
            else:
                novaInformacao += letraNova
        #adiciona a novaInformacao nas viriáveis dependendo da etapa atual
        else:
            estadosADF= adicionarEstado(novaInformacao, etapaAtualIndex)
            novaInformacao = None

            
    #quando encontrar um \n passa para a próxima etapa até a transferência
    estadosADF = adicionarEstado(novaInformacao, etapaAtualIndex)
    novaInformacao = None
    etapaAtualIndex += 1

ADF = criarADF(estadosADF)

for verificacao in range(len(estadosADF[-1])): 
        resultado = ADF(estadosADF[-1][verificacao])
        print(resultado)