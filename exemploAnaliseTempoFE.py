import numpy as np
import matplotlib.pyplot as plt
from estampas import Estampa

C = 2e-3
deltaT = 0.1e-3
tempoFinal = 20e-3

# Criando a fonte pulse
nPontos = int(tempoFinal/deltaT)
eTran = np.zeros(nPontos)
iIn = 10*np.ones(nPontos)
iIn[:11] = np.linspace(0,10,11)
tempo = np.linspace(0,tempoFinal,nPontos)
#tempo = np.arange(0,tf+deltaT,deltaT)
plt.plot(tempo*1e3,iIn) # Em milisegundos


e = [0,0]

for iPonto in range(1,nPontos):

    Gn = np.zeros([3,3])
    In = np.zeros(3)

    Gn = Estampa.resistor(1,0,1,Gn)
    In = Estampa.fonteCorrente(iIn[iPonto],0,1,In)

    Gn,In = Estampa.capacitorFE(C,deltaT,e[0],e[1],2,1,0,Gn,In)

    e = np.linalg.solve(Gn[1:,1:],In[1:])
    print(e)
    eTran[iPonto] = e[0]


plt.plot(tempo*1e3,eTran)

plt.show()