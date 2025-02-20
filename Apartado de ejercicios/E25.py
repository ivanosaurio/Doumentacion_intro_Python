'''Combinar 2 listas en pares usando zip()''' #Esto es util para cuando necesitamos asociar 2 valores de una lista con otro de formaque creen un conjunto

lista1 = [2, 3, 34, 5, 6, 4, 23, 234, 2, 43, 43]
lista2 = [12, 23, 23, 24, 3345, 384628956]

Combinar = list(zip(lista1, lista2))
print (Combinar)

usuarios = {'pedro', 'paco', 'chucho'}
contraseñas = {'ayudapls', 'ola que hace', 'renacuajo'}
Credenciales = list(zip(usuarios, contraseñas))
print (Credenciales)
#Ejemplo muy clasico de una base de datos asociada a an usuario y una contraseña