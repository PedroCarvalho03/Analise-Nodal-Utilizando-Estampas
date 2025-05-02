import numpy as np
from estampas import Estampa

# Definicndo Parametros

R1 = 1
R2 = 1

C1 = 1
C2 = 1

L1 = 2

I1 = 1

omega = 1 

Gn = np.zeros((3,3),dtype='complex')
In = np.zeros(3)

# Adicionando as Estampas as matrizes

Estampa.resistor(R1,0,1,Gn)
Estampa.resistor(R2,0,2,Gn)

Estampa.capacitor(C1,omega,1,0,Gn)
Estampa.capacitor(C2,omega,2,0,Gn)

Estampa.indutor(L1,omega,1,2,Gn)

Estampa.fonteCorrente(I1,0,1,In)

# Tirando a linha do Terra
Gn = Gn[1:,1:] 
In = In[1:]

# Resolver o Sistema
e = np.linalg.solve(Gn,In)


if __name__ == "__main__":
    print(Gn)
    print('-----x-----')
    print(In)
    print('-----x-----')
    print(e)

