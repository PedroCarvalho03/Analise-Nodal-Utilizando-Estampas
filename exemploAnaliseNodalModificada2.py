import numpy as np
from estampas import Estampa

# Definindo parametros do sistema

R1 = 1
R2 = 2
R3 = 1

I1 = 1

V1 = 2

Gm = 1

A = 2

B = 1 


Gn = np.zeros((8,8))
In = np.zeros(8)

# Adicionando as Estampas as matrizes

Estampa.resistor(R1,0,2,Gn)
Estampa.resistor(R2,0,3,Gn)
Estampa.resistor(R3,3,4,Gn)

Estampa.fonteCorrenteControladaTensão(Gm,2,4,3,0,Gn)

Estampa.fonteCorrente(I1,0,1,In)

Estampa.fonteTensao(V1,6,3,1,Gn,In)

Estampa.fonteTensaoControladaTensao(A,7,4,0,2,4,Gn)

Estampa.fonteCorrenteControladaCorrente(B,5,3,0,1,2,Gn)



# Retirando linha do terra

Gn = Gn[1:,1:]
In = In[1:]

# Resolve o sistema

#e = np.linalg.solve(Gn,In)
if __name__ == "__main__":
    print(Gn)
    print('-----x-----')
    print(In)
    print('-----x-----')
    #print(e)