import random as rd

class Pile:
    '''création d'une instance Pile avec une liste'''
    def __init__(self):
        "Initialisation d'une pile vide"
        self.L=[]
        self.taille=0

    def vide(self):
        "test si la pile est vide en retournant Vrai si c’est le cas"
        if self.taille==0:
            return True
        else:
            return False

    def depiler(self):
        assert(self.taille>0)
        "retourne la pile à laquelle on a enlevé le sommet "
        self.taille-=1
        return self.L.pop()

    def empiler(self,x):
        "retourne la pile avec pour sommet x"
        self.taille+=1
        self.L.append(x)
    
    def longueur(self):
        return self.taille
    
    def sommet(self):
        assert (self.vide()==False)
        return self.L[self.taille-1]
    
    def melange(self):
        return  rd.shuffle(self.L)
    
    







