import numpy as np
from numpy import sqrt,cos,sin,pi

tau = @valeur taux compression@ #[-] = Volume au point mort bas PMB (vol max) / volume au point mort haut PMH (vol min)
# pour l essence le taux vaire de 1.0 a 1.2 MPa et pour le diesel de 3.0 a 3.5 MPa
D = @valeur alesage@ #[m] = diametre du cylindre dans lequel le piston rentre
C = @valeur course@ #[m] = la course est le déplacement du piston donc max de 2R

L = @valeur longueur bielle@  # [m] = la tige entre le piston et le vilebrequin ( relié au maneton du vilebrequin )
mpiston = @valeur masse piston@ #[kg] =
mbielle = @valeur masse bielle@ #[kg] = connecting rod
Q = @valeur chaleur emise par fuel par kg de melange admis@ #[J/kg_inlet gas]

#Deux directions de flambages ?

R=C/2 @distance entre le maneton et le tourillon@ #en [m]

#theta en degre ss forme d un vecteur de - 180 a 180
#Mais on va simuler un cycle complet ? donc 2* 360 ?
theta= np.arange(-180*2,180*2,5)
H=np.zeros(len(theta))
V_output=np.zeros(len(theta))
def V_cyl(L,R,theta,D):
    b=L/R
    for index,j in enumerate(theta,-180*2):
        h=R*(1-cos(theta)+b-sqrt(b**2-sin(theta)**2))
        H[index]=h
        V_output=H*pi*(D/2)**2
    return V_output
la tu vois direct
def apport_chaleur(): # calculer l'apport de chaleur sur la durée de temps de combustion voir son schéma 
    return Q_output # en [J]

def force_bielle():
    return F_pied_output et F_tete_output # en [N]

def pression_cylindre():
    return p_output # en [Pa]

def epaisseur_critique(): #? voir schema de l enonce
    return t  # en [m]


def myfunc(rpm, s, theta, thetaC, deltaThetaC):
    #VOTRE CODE
    return (V_output, Q_output, F_pied_output, F_tete_output, p_output, t)  #v
