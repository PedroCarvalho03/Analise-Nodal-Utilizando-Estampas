import numpy as np

class Estampa():

    @staticmethod
    def resistor(R,a,b,Gn):
        Gn[a][a] += 1/R
        Gn[a][b] += -1/R
        Gn[b][a] += -1/R
        Gn[b][b] += 1/R
    
    @staticmethod
    def fonteCorrenteControladaTensão(Gm,a,b,c,d,Gn):
        Gn[a][c] += Gm
        Gn[a][d] += -Gm
        Gn[b][c] += -Gm
        Gn[b][d] += Gm
    
    @staticmethod
    def fonteCorrente(I,a,b,In):
        In[a] = -I
        In[b] = I

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
        
    
        
    
    

    
        
    