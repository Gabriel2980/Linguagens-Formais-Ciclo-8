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

#Guardando todo o input do site para criar o automato
automato = input()

#criando os índex para as etapas de criação da ADF 
estadosIndex=0
etapaAtualIndex = 0
estadosAceitacaoIndex=0
alfabetoIndex = 0
transferenciaIndexAlfabeto = 0
transferenciaIndexEstados = 0
transferenciaIndex = 0

novaInformacao = None

#criando todas etapas da ADF
etapaDeCriacaoDaADF = ['CriandoEstados', 'EstadoInicial', 'EstadosDeAceitacao', 'CriandoAlfabeto', 'Transferencia']
etapaAtual = etapaDeCriacaoDaADF[etapaAtualIndex]

for letraNova in automato: 

    #adiciona uma letra na string novaInformacao até encontrar um espaço
    if(letraNova != ' '):
        if(letraNova != '\n')
            if(novaInformacao == None):
                novaInformacao = letraNova
            else:
                novaInformacao += letraNova
        
        #quando encontrar um \n passa para a próxima etapa até finalizar todas etapas
        elif(etapaAtualIndex < len(etapaDeCriacaoDaADF)):
            etapaAtualIndex += 1
            etapaAtual = etapaDeCriacaoDaADF[etapaAtualIndex]
        #ao finalizar todas etapas para criar a ADF verifica se os símbolos são aceitos ou rejeitados
        elif(len(transferencia) >= len(estados)):
            resultado = AFD(novaInformacao)

    #adiciona a novaInformacao nas viriáveis dependendo da etapa atual
    else:
        if(etapaAtual == 'CriandoEstados'):
            #guarda os estados aumentando o index até passar para a próxima etapa
            estados[estadosIndex] = novaInformacao
            estadosIndex += 1

        elif(etapaAtual == 'EstadoInicial'):
            #guarda o estado inicial
            estadoInicial = novaInformacao

        elif(etapaAtual == 'EstadosDeAceitacao'):
            #guarda estados de aceitação aumentando o index até passar para a próxima etapa
            estadosAceitacao[estadosAceitacaoIndex] = novaInformacao
            estadosAceitacaoIndex += 1

        elif(etapaAtual == 'CriandoAlfabeto'):
            #guarda o alfabeto aumentando o index até passar para a próxima etapa
            alfabeto[alfabetoIndex] = novaInformacao
            alfabetoIndex += 1
        
        #transferencia
        else:
            if(transferenciaIndexAlfabeto < alfabetoIndex):
                transferencia[transferenciaIndexEstados][transferenciaIndexAlfabeto] = novaInformacao
                transferenciaIndexAlfabeto += 1
            elif(transferenciaIndexEstados < estadosIndex):
                transferenciaIndexEstados += 1
