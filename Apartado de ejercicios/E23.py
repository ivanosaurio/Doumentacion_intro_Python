'''Operaciones con conjuntos, uniones e intersecciones'''
conjuto = {'paco', 'pedro', 'juanito', 'ricardo'}
conjunto2 = {'paco', 'oscar', 'juancho', 'emanuel'}

union = conjuto | conjunto2 #Unir ambos conjuntos
interseccion = conjuto & conjunto2 #El numero que se interpone entre ambos conjuntos (Muy util para encontrar personas o cosas que estan repetidas en lugares que no deberian)

print ( union)
print ( interseccion)