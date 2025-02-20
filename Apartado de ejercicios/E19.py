'''Verificar si una palabra es un palindromo'''
palabra = 'olo'
verificacion = palabra == palabra[::-1]
if verificacion == True:
    print('Felicidades tienes un palindromo')
else:
    print ('Que weona es eso, un palindromo ño :v')