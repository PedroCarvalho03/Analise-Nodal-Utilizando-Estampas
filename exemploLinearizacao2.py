import numpy as np
from estampas import Estampa

GnInicial = np.zeros([3,3])
InInicial = np.zeros(3)

GnInicial = Estampa.resistor(2,1,2,GnInicial)
InInicial = Estampa.fonteCorrente(2,0,1,InInicial)

eAnterior = np.array([0,1.5,0])
numIteracoes = 100
tol = 1e-5

while numIteracoes > 0:

    Gn = GnInicial.copy()
    In = InInicial.copy()

    Gn,In = Estampa.resistorQuadratico(eAnterior,1,0,Gn,In)
    Gn,In = Estampa.fonteCorrenteControladaTensaoLinearizado(eAnterior,2,0,1,2,Gn,In)


    eAtual = np.linalg.solve(Gn[1:,1:],In[1:])
    # Voltar a ter o terra para proxima iteracao
    eAtual = np.concatenate([np.array([0]),eAtual])

    if np.max(np.abs(eAtual-eAnterior)) < tol:
        break
    
    print(eAtual)
    eAnterior = eAtual

    numIteracoes -=1

print(eAtual)