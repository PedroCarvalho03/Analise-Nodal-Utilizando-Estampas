import numpy as np
from estampas import Estampa

# Definindo parametros do sistema

R1 = 1
R2 = 2
R3 = 1

I1 = 1

V1 = 1

Gm = 1

Gn = np.zeros((5,5))
In = np.zeros(5)

# Adicionando as Estampas as matrizes

Estampa.resistor(R1,1,3,Gn)
Estampa.resistor(R2,0,2,Gn)
Estampa.resistor(R3,2,3,Gn)

Estampa.fonteCorrenteControladaTensão(Gm,0,3,3,1,Gn)

Estampa.fonteCorrente(I1,2,1,In)

Estampa.fonteTensao(V1,4,1,0,Gn,In)

# Retirando linha do terra

Gn = Gn[1:,1:]
In = In[1:]

# Resolve o sistema

e = np.linalg.solve(Gn,In)
if __name__ == "__main__":
    print(Gn)
    print('-----x-----')
    print(In)
    print('-----x-----')
    print(e)