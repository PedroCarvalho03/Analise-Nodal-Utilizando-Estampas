import numpy as np

class Estampa():

    @staticmethod
    def resistor(R,a,b,Gn):
        Gn[a][a] += 1/R
        Gn[a][b] += -1/R
        Gn[b][a] += -1/R
        Gn[b][b] += 1/R
        return Gn

    @staticmethod
    def fonteCorrenteControladaTensão(Gm,a,b,c,d,Gn):
        Gn[a][c] += Gm
        Gn[a][d] += -Gm
        Gn[b][c] += -Gm
        Gn[b][d] += Gm
        return Gn
    
    @staticmethod
    def fonteCorrente(I,a,b,In):
        '''
        a->b
        '''
        In[a] -= I
        In[b] += I
        return In

    @staticmethod
    def capacitor(C,omega,a,b,Gn):
        Gn[a][a] += 1j*omega*C
        Gn[a][b] += -1j*omega*C
        Gn[b][a] += -1j*omega*C
        Gn[b][b] += 1j*omega*C

    @staticmethod
    def capacitorLaplace(C,s,a,b,Vab0,Gn,In):
        Gn[a][a] += s*C
        Gn[a][b] += -s*C
        Gn[b][a] += -s*C
        Gn[b][b] += s*C
        In[a] += C*Vab0
        In[b] += -C*Vab0
    
    @staticmethod
    def indutor(L,omega,a,b,Gn):
        Gn[a][a] += 1/(1j*omega*L)
        Gn[a][b] += -1/(1j*omega*L)
        Gn[b][a] += -1/(1j*omega*L)
        Gn[b][b] += 1/(1j*omega*L)

    
    @staticmethod
    def capacitorLaplace(L,s,a,b,Iab0,Gn,In):
        Gn[a][a] += 1/(s*L)
        Gn[a][b] += -1/(s*L)
        Gn[b][a] += -1/(s*L)
        Gn[b][b] += 1/(s*L)
        In[a] += -Iab0/s
        In[b] += Iab0/s
    
    @staticmethod
    def fonteTensao(V,x,a,b,Gn,In):
        Gn[a][x] += 1 
        Gn[b][x] += -1
        Gn[x][a] += -1
        Gn[x][b] += 1
        In[x] += -V
        return Gn,In
    
    @staticmethod
    def fonteTensaoControladaTensao(A,x,a,b,c,d,Gn):
        Gn[a][x] += 1 
        Gn[b][x] += -1
        Gn[x][a] += -1
        Gn[x][b] += 1
        Gn[x][c] += A
        Gn[x][d] += -A
        
    @staticmethod
    def fonteCorrenteControladaCorrente(B,x,a,b,c,d,Gn):
        Gn[a][x] += B 
        Gn[b][x] += -B
        Gn[c][x] += 1
        Gn[d][x] += -1
        Gn[x][c] += -1
        Gn[x][d] += 1
    
    
    @staticmethod
    def fonteTensaoControladaCorrente(Rm,x,y,a,b,c,d,Gn):
        Gn[a][y] += 1 
        Gn[b][y] += -1
        Gn[c][x] += 1
        Gn[d][x] += -1
        Gn[x][c] += -1 
        Gn[x][d] += 1
        Gn[y][a] += -1
        Gn[y][b] += 1
        Gn[y][x] += Rm
        
    
    @staticmethod
    def resistorQuadratico(e,a,b,Gn,In):
        '''
        a -> Nó Positivo,
        b -> Nó Negativo
        '''
        G0 = 2*(e[a]-e[b])
        I0 = (e[a]-e[b])**2 - G0*(e[a]-e[b])

        G = Estampa.resistor(1/G0,a,b,Gn)
        I = Estampa.fonteCorrente(I0,a,b,In)
        
        return G,I
    
    @staticmethod
    def fonteCorrenteControladaTensaoLinearizado(e,a,b,c,d,Gn,In):
        '''
        a -> b,
        c -> Controle +
        d -> Controle -
        '''

        Gm = -1/(e[c]-e[d])**2
        I0 = 1/(e[c]-e[d]) - Gm*(e[c]-e[d])

        G = Estampa.fonteCorrenteControladaTensão(Gm,a,b,c,d,Gn)
        I = Estampa.fonteCorrente(I0,a,b,In)

        return G,I

    @staticmethod
    def capacitorBE(c,deltaT,v0,a,b,Gn,In):
        '''noA(+) o-||-o noB(-)'''
        G = Estampa.resistor(deltaT/c,a,b,Gn)
        I = Estampa.fonteCorrente(c/deltaT*v0,b,a,In)
        return G,I

    @staticmethod
    def capacitorFE(c,deltaT,v0,i0,x,a,b,Gn,In):
        '''noA(+) o-||-o noB(-)'''
        Gn[a,x] += 1
        Gn[b,x] -= 1

        Gn[x,a] += 1
        Gn[x,b] -= 1

        In[x] += v0+deltaT/c*i0
        
        return Gn,In

        
        
    