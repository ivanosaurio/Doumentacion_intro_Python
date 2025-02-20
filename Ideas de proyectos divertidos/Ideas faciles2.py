'''Una aplicacion que te permita convertir tus palabras a palindromos'''
palabra = input('Ingrese su palabra de favor:')
if palabra == palabra[::-1]:
    print ('Esto ya es un palindromo')
else:
    print('Tu palindromo seria este:', palabra + palabra[::-1])