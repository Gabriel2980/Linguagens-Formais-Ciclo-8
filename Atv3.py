import math

def criarADF(estados, estadosFuturos,estadoInicial, estadosAceita, alfabeto, transferencia):
    estados

def AFD(estado, simboloNovo):
    if(simboloNovo != '0' and simboloNovo != '1'):
        return estado
    if(estado == 'q1'):
        if(simboloNovo == '0'):
            estado = 'q1'
        else:
            estado = 'q2'
    elif(estado == 'q2'):
        if(simboloNovo == '0'):
            estado = 'q3'
        else:
            estado = 'q2'
    elif(estado == 'q3'):
        estado = 'q2'
    return estado

estado = 'q1'
resultado = 'rejeitado'

automato = input()
i=0
todosEstados = None
novaInformacao = None
etapaDeCriacaoDaADF = ['CriandoEstados', 'EstadoInicial', 'EstadosDeAceitacao', 'CriandoAlfabeto', 'Transferencia']
etapaAtualIndex = 0
etapaAtual = etapaDeCriacaoDaADF[etapaAtualIndex]
estados = None

for estado in automato: 

    #adiciona uma letra na string novaInformacao até encontrar um espaço
    if(estado != ' '):
        if(novaInformacao == None):
            novaInformacao = estado
        else:
            novaInformacao += estado
        
        #quando encontrar um \n passa para a próxima etapa até finalizar todas etapas
        if(estado == '\n' and etapaAtualIndex < len(etapaDeCriacaoDaADF)):
            etapaAtualIndex += 1
            etapaAtual = etapaDeCriacaoDaADF[etapaAtualIndex]
    else:
        if(etapaAtual == 'CriandoEstados'):
            #ao encontrar um /n cria o estado inicial e passa para a próxima etapa dos estados de aceitação
            if(estado != '\n'):
                estados[i] = novaInformacao
                i += 1
            else:
                estadoInicial = novaInformacao

        elif(etapaAtual == 'EstadoInicial'):
            #enquanto não encontrar um /n vai adicionando os estados de aceitação
            #ao encontrar um /n passa para a próxima etapa de criar o alfabeto
            estadoInicial = novaInformacao

        elif(etapaAtual == 'EstadosDeAceitacao'):
            #enquanto não encontrar um /n vai adicionando os estados de aceitação
            #ao encontrar um /n passa para a próxima etapa de criar o alfabeto
            if(estado != '\n'):
                estados[i] = novaInformacao
                i += 1
            else:
                estadoInicial = novaInformacao