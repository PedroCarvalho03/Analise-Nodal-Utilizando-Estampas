import numpy as np

def matrizFuncao(e):
    funcaoE1 = e[0]**2 + (e[0]-e[1])/2 - 2
    funcaoE2 = (e[1]-e[0])/2 + 1/(e[0]-e[1])
    return np.array([funcaoE1,funcaoE2])

def jacobianoFuncao(e):
    derivadaParcialE1PosZero = 0.5 + 2*e[0] 
    derivadaParcialE1PosUm = -0.5
    derivadaParcialE2PosZero = - 0.5 - 1/(e[0]-e[1])**2
    derivadaParcialE2PosUm = 0.5 + 1/(e[0]-e[1])**2
    return np.array([[derivadaParcialE1PosZero,derivadaParcialE1PosZero],
                     [derivadaParcialE2PosZero,derivadaParcialE2PosUm]])

eAnterior = np.array([1.5,0])
numIteracoes = 100
tol = 1e-10

while numIteracoes > 0:

    jacobiano = jacobianoFuncao(eAnterior)

    eAtual = eAnterior - np.linalg.inv(jacobiano).dot(matrizFuncao(eAnterior))

    if np.max(np.abs(eAtual-eAnterior)) < tol:
        break

    print(eAtual)

    eAnterior = eAtual

    numIteracoes-=1

print(eAtual)