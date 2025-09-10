import math

def criarADF(estados):

    def ADF(simboloNovo):
        estadoAtual = estados[1][0]
        for simbolo in simboloNovo:
            for i in range(len(estados[0])):
                if(estados[0][i] == estadoAtual):
                    break
            for j in range(len(estados[3])):
                if(estados[3][j] == simbolo):
                    break
            estadoAtual = estados[i+4][j+1]
        if(estadoAtual in estados[2]):
            resultado = 'aceita'
        else:
            resultado = 'rejeita'
        return resultado
    return ADF

def adicionarEstado(novaInformacao, etapaAtualIndex):
    if(len(estadosADF) <= etapaAtualIndex):
        estadosADF.append([])
    estadosADF[etapaAtualIndex].append(novaInformacao)
    return estadosADF

#criando os índex para as etapas de criação da ADF 
etapaAtualIndex = 0
transferenciaIndex = 0

novaInformacao = None

#criando matriz para guardar os estados, estados de aceitação, alfabeto e transferência
estadosADF = []

#criando todas etapas da ADF
etapaDeCriacaoDaADF = ['CriandoEstados', 'EstadoInicial', 'EstadosDeAceitacao', 'CriandoAlfabeto', 'Transferencia']

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
        novaInformacao = None