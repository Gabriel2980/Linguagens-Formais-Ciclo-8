#Testa se mais estados devem entrar junto do estado novo
def entrandoEmEstado(estados, estados_lista, estadosPossiveis):

    estadosPossiveis.append(estados_lista)
    estados_lista_Extras = []
    if(estados[4+int(estados_lista[-1])-int(estados[4][0][-1])][-1] != 'vazio'):
                        estados_lista_Extras = estados[4+int(estados_lista[-1])-int(estados[4][0][-1])][-1].split(',')
    for todosCasos in range(len(estados_lista_Extras)):  
        estadosPossiveis.append(estados_lista_Extras[todosCasos])
    
    return estadosPossiveis

#cria a ADF
def ADF(simboloNovo, estados):
    estadosPossiveis = []
    estadosPossiveis = entrandoEmEstado(estados, estados[2][0], estadosPossiveis)
    #Verifica todos os simbolos da palavra
    for simbolo in simboloNovo:
        #copia os estadosPossiveis para ela não alterar durante o loop
        copiaEstadosPossiveis = estadosPossiveis.copy()
        print(estadosPossiveis)
        print(simbolo)
        #verifica os simbolos em cada estado possível
        for estadoAtual in copiaEstadosPossiveis:
            
            #encontra o index do estado atual e do simbolo atual
            for i in range(len(estados[0])):
                if(estados[0][i] == estadoAtual):
                    break
            for j in range(len(estados[1])):
                if(estados[1][j] == simbolo):
                    break
            #verifica se existem mais de 1 estado possível
            estados_lista = estados[i+4][j+1].split(',')

            #adiciona todos estados na lista de estadosPossiveis        
            for todosCasos in range(len(estados_lista)):
                if(estados[i+4][j+1] != 'vazio'):
                    estadosPossiveis = entrandoEmEstado(estados, estados_lista[todosCasos], estadosPossiveis)
            #remove o estado que foi estudado e atualizado
            estadosPossiveis.pop(0)
    
    print(estadosPossiveis)
    resultado = 'rejeita'
    #se o estado aceito for um dos estadosPossiveis, a palavra é aceita
    for estadoAtual in estadosPossiveis:
        if(estadoAtual in estados[3]):
            resultado = 'aceita'
    return resultado

#adiciona estados para criar a ADF
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

#realiza o loop para criar a ADF pela quantidade de etapaDeCriacaoDaADF, mais a quantidade de estados para a transferência
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
        #adiciona a novaInformacao nas variáveis dependendo da etapa atual
        else:
            estadosADF= adicionarEstado(novaInformacao, etapaAtualIndex)
            novaInformacao = None

            
    #quando encontrar um \n passa para a próxima etapa
    estadosADF = adicionarEstado(novaInformacao, etapaAtualIndex)
    novaInformacao = None
    etapaAtualIndex += 1

#verifica todas palavras    
for verificacao in range(len(estadosADF[-1])): 
        resultado = ADF(estadosADF[-1][verificacao], estadosADF)
        print(resultado)