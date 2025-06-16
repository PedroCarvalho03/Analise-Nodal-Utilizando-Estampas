import numpy as np

def funcao(x):
    return x**2 + (x/2) - 0.5

def derivadaFuncao(x):
    return 2*x + 0.5

eAnterior = 2 # Condicao Inicial
numIteracao = 100


while numIteracao > 0:

    eAtual = eAnterior - funcao(eAnterior)/derivadaFuncao(eAnterior)

    if np.abs((eAtual-eAnterior)) < 0.00001:
        break
    
    print(eAtual)
    eAnterior = eAtual

    numIteracao -=1

print(eAtual)