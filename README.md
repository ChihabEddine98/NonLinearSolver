# Non Linear Equations
## Méthode de Newton
 Tout d'abord ,il faut installer la bibliotheque [sympy](https://www.sympy.org/en/index.html "sympy doc") qu'on utilisera plus tard.Assurez-vous aussi de travailler sous une machine Linux et de Python 3.
 > pip install sympy 
 
 Les fonctions en relation avec cette méthode se trouvent dans le fichier [newton.py](newton.py) et les tests unitaires se font dans le fichier [test_newton.py](test_newton.py).
 Il faut donc,pour tester, lancer la commande:
 > **python3 test_newton.py**
 
 Nous avons implémentés deux versions différentes de cette méthode:
 * **res_equa_newton(f,Df,x0,epsilon,max_iter)**:
 	* La fonction classique, qui prend en argument:
	  * f : une fonction f 
	  * Df : la dérivée de f
	  * x_0  : une valeur approchée initiale
	  * epsilon : le seuil de tolérance 
	  * max_iter : le nombre maximum d'itérations permis
	 
 * **res_equa_newton_withoutDf(f,x0,epsilon,max_iter)**:
 	* La fonction qui calcule directement la dérivée d'une fonction f ,à l'aide de [sympy](https://www.sympy.org/en/index.html "sympy doc")
 	  * f : une fonction f 
	  * x0  : une valeur approchée initiale
	  * epsilon : le seuil de tolérance 
	  * max_iter : le nombre maximum d'itérations permis
 
## Méthode de Dichotomie

les fonctions en relation avec cette méthode se trouvent dans le fichier 
**`dichotomie.py`** et des tests sont disponibles sur **`main.py`** 
pour pouvoir lancer un test ( pour l'instant les fonctions pour tester cette méthode
déjà fournies  dans le fichier **`tests.py`**  ) il faut donc lancer la commande : 
>**python3 main.py**

TODO --- 
1)Screenshots
2)English version 
3)Doc
4)SGD
5) ADABOOST SGD
6) MACOS version
