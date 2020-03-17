



"""
    res_equa_dct(f,a,b)

    Cette fonction résout l'equation f(x)=0 
    pour une fonction f monotonne (croissante ou décroissante)
    sur un intervale [a,b] le pseudo code de cette fonction
    est disponible sur le ReadMe du dépot  
"""

def res_equa_dct(f,a,b,err):    
    debut=a
    fin=b
    while ( fin-debut > err ):
        millieu=(debut+fin)/2
        if ( f(debut)*f(millieu) < 0):
            fin=millieu
        else:
            debut=millieu

    return millieu




