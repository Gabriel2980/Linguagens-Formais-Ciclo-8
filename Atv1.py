import math

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

palavra = input()
i=0
for simboloNovo in palavra: 
    estado = AFD(estado, simboloNovo)
    if(estado == 'q2'):
        resultado = 'aceita'
    else:
        resultado = 'rejeita'
    if(simboloNovo == ' ' or i == len(palavra)-1):
        print(resultado)
        estado = 'q1'


    i += 1