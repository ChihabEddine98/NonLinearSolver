# NonLinear-Equations

# Méthode de Dichotomie

les fonctions en relation avec cette méthode se trouvent dans le fichier 
`dichotomie.py` et des tests sont disponibles sur `main.py` 
pour pouvoir lancer un test ( pour l'instant les fonctions pour tester cette méthode
déjà fournies ) il faut donc lancer la commande : 
>python3 main.py

**res_equa_dct (f , a , b , err) :**
-
Cette fonction résout l’équation f(x)=0 pour une fonction f monotone (croissante ou décroissante)sur un intervalle [a,b] le pseudo code de cette fonction
est en dessous : 
```
------------------------------------------------------------------------
parametres à passer :
			f   : une fonction monotone 
			a,b : les bornes de l'intervalle [a,b]
			err : l'erreur pour le calcul approché de la solution
------------------------------------------------------------------------
# Méthode Dichotomie 

Début
debut <- a
fin   <- b

TantQue ( fin-debut > err )
{
    millieu = (debut + fin ) / 2
    
    Si  ( f(millieu) >  0 )
    {
	    fin <- millieu
    } 
    Sinon 
    {
        debut <- millieu
    }
}
retourner (millieu) 
```
