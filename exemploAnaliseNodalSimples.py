import numpy as np
from estampas import Estampa

# Definindo os paramêtros dos componentes
R1 = 1
R2 = 2
R3 = 3
R4 = 4
R5 = 5
R6 = 6

Gm = 1

I1 = 1
I2 = 2

Gn = np.zeros((5,5))
In = np.zeros(5)

# Adicionando as Estampas nas matrizes
Estampa.resistor(R1,0,1,Gn)
Estampa.resistor(R2,1,2,Gn)
Estampa.resistor(R3,0,2,Gn)
Estampa.resistor(R4,1,3,Gn)
Estampa.resistor(R5,0,4,Gn)
Estampa.resistor(R6,2,4,Gn)

Estampa.fonteCorrenteControladaTensão(Gm,3,4,1,3,Gn)

Estampa.fonteCorrente(I1,0,1,In)
Estampa.fonteCorrente(I2,4,2,In)

# Eliminar a Linha do Terra
Gn = Gn[1:,1:]
In = In[1:]

# Calcular a matriz e

e1 = np.linalg.solve(Gn,In) # Resolve o sistema

GnInv = np.linalg.inv(Gn) # Calcula a inversa
e2 = GnInv.dot(In) # .dot faz a multiplicacao de matrizes

if __name__ == "__main__":
    print(Gn)
    print('-----x-----')
    print(In)
    print('-----x-----')
    print(GnInv)
    print('-----x-----')
    print(e1)
    print('-----x-----')
    print(e2)