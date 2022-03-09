import matplotlib.pyplot as plt

import Pile as pl






class Labyrinthe:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.cells=[]
        for i in range(self.width):
            ligne=[]
            for j in range(self.height):
                ligne.append({'E': False, 'N': False, 'S': False, 'O': False, 'zone':j+5*i})
            self.cells.append(ligne)
        self.ouvert=0
        
    
    def print_plot(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j]['N']==False:
                    plt.plot([j,j+1],[self.height-i,self.height-i], color='yellow')
                if self.cells[i][j]['S']==False:
                    plt.plot([j,j+1],[self.height-(i+1),self.height-(i+1)], color='yellow')
                if self.cells[i][j]['O']==False:
                    plt.plot([j,j],[self.height-i,self.height-(i+1)],color='yellow')
                if self.cells[i][j]['E']==False:
                    plt.plot([j+1,j+1],[self.height-i,self.height-(i+1)],color='yellow')
        plt.show()
   
   
    def peindre(self,i,j,orig,val):
        if i>self.height-1 or i<0 or j<0 or j>self.width-1:
            return None
        if self.cells[i][j]['zone']==val:
            self.cells[i][j]['zone']=orig
            self.peindre(i-1,j,orig,val)
            self.peindre(i+1,j,orig,val)
            self.peindre(i,j-1,orig,val)
            self.peindre(i,j+1,orig,val)
            
    
    def fusionner(self,i,j,dir):
        zone=self.cells[i][j]['zone']
        if dir=='E' and self.cells[i][j+1]['zone']!=zone:
            self.ouvert+=1
            self.cells[i][j]['E']=True
            self.cells[i][j+1]['O']=True
            self.peindre(i,j+1,zone,self.cells[i][j+1]['zone'])
            
        elif dir=='O' and self.cells[i][j-1]['zone']!=zone:
            self.ouvert+=1
            self.cells[i][j]['O']=True
            self.cells[i][j-1]['E']=True
            self.peindre(i,j-1,zone,self.cells[i][j-1]['zone'])
            
        elif dir=='N' and self.cells[i-1][j]['zone']!=zone:
            self.ouvert+=1
            self.cells[i][j]['N']=True
            self.cells[i-1][j]['S']=True
            self.peindre(i-1,j,zone,self.cells[i-1][j]['zone'])
            
        elif dir=='S' and self.cells[i+1][j]['zone']!=zone:
            self.ouvert+=1
            self.cells[i][j]['S']=True
            self.cells[i+1][j]['N']=True
            self.peindre(i+1,j,zone,self.cells[i+1][j]['zone'])
            
        else:
            return False
          
          
    def generer(self):
        murs=pl.Pile()
        for i in range(self.height):
            for j in range(self.width):
                if j!=self.width-1:
                    murs.empiler((i,j,'E'))
                if j!=0:
                    murs.empiler((i,j,'O'))
                if i!=self.height-1:
                    murs.empiler((i,j,'S'))
                if i!=0:
                    murs.empiler((i,j,'N'))
        murs.melange()
        while  self.ouvert<self.width*self.height-1 and not murs.vide():
            self.fusionner(murs.sommet()[0],murs.sommet()[1],murs.sommet()[2])
            murs.depiler()
       
                
    
laby=Labyrinthe(5,5)
laby.generer()
laby.print_plot()
