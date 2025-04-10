 # exo 1

import Exercices_NumPy_Pratique.numpy as np

matrice = np.arange(10, 30).reshape(4, 5)

print("Nombre de dimensions :", matrice.ndim)
print("Forme du tableau :", matrice.shape)
print("Type des éléments :", matrice.dtype)

print("Moyenne :", matrice.mean())
print("Écart-type :", matrice.std())
print("Maximum :", matrice.max())

aplat = matrice.flatten()
matrice_5x4 = aplat.reshape(5, 4)

print("Tableau aplati :", aplat)
print("Reconverti en 5x4 :\n", matrice_5x4)


 # exo 2

a = np.arange(0, 10)
b = np.arange(10, 20)

a_mat = a.reshape(2, 5)
b_mat = b.reshape(2, 5)

somme = a_mat + b_mat
print("Somme des matrices :\n", somme)

concat_h = np.hstack((a_mat, b_mat))
concat_v = np.vstack((a_mat, b_mat))

print("Concaténation horizontale :\n", concat_h)
print("Concaténation verticale :\n", concat_v)
print("Deuxième ligne concaténée verticalement :", concat_v[1])
