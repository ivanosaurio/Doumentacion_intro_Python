#Variables
#una variable sirve para almacenar informacion que puede cambiar
#digamos que tenemos una aplicacion, y queremos que cada usuario tenga un nombre especifico y unico, bueno, lo que hariamos seria hacer una VARIABLE, que nos muestre el nombre de usuario especifico de cada quien
#e.g
a = "tu mama "
b = "es tremenda mamu "
c = (a + b)
print (c)
#esto en la terminal da como: tu mama es tremenda mamu

#ahora, es importante tener en cuenta lo siguiente:
#las variables tienen una forma concreta de funcionar
#Paso 1: Declarar la variable
# Paso 2: Definirla
#para declarar una varibale basta con simplemente escribir el nombre de la variable sin las comillas, para que el programa entienda que es una variable, y no un texto
#y para definirla, hace falta darle un (=) que es la forma de decirle al programa que hace la variable que declaramos previamente

#e.g
holapapu = "hola"

#hola papu es el nombre de la variable (por eso se ve en azul) y #hola" es el equivalente que cumple la variable, que en este caso es un textoque dice (hola). De modo que si nosotros le decimos al programa que nos muestre (holapapu) lo que nos va a mostrar en la terminal va a ser un text que contenga la palabra (hola)

print (holapapu)

#las variables pueden ser actualizadas, de modo que si nosotros decidimos que una variable ya no es (x) y ahora es (y) lo podemos especificar en las variables

#e.g
numero = 1
numero = 2
print (numero)
#= 2

#cuando nosotros le decimos que nos muestre la variable (numero) lo que va a hacer es mostrarnos 2, ya que las actualizaciones de las variables se van a dar en base a la viriable del mismo nombre que este mas abajo en las lineas de codigo
#pero, supongamos que nosotros queremos agregar una actualizacion a la variable ya establecida (queremos agregar algo nuevo a la variable que ya escribimos antes)
#bueno, lo que hacemos es poner un + en la variable antes de imprimirla

#e.g
numero = 2
numero += 7
print (numero) 
#= 9

#e.g2
a += b
print (a)
#resultado igual, pero asi agregamos variables entre si, no actualizaciones de la misma variable

#e.g3
#print (a + numero)
#nota: no se pueden agregar variables de tipos de datos distintos entre si (o al menos no de esta forma)
#peeero, si se puede concatenar (agregar) una variable de texto con una variable de numero, si el resultado es un tipo de texto,utilzando la concatenazion de (f string). Esto siginifica que independientemente de el tipo de dato que obtengamos de la base de datos, el (f string) siempre lo va a convertir en texto

#e.g4"
print (a + f"{numero}")
#como se ve, la variable (a) es de tipo texto, y la variable (numero)  es de tipo numero, de modo que para que el programa se pueda leer como una linea entera de texto,se tiene que poner la variable que queremos convertir en texto entre corchetes, utilizar comillas rodeando dichos corchetes, y agregando la letra (f) al inicio de todo esto, para dar a entender al programa que queremos concatenar un formato numero con un formato tecto, y que el resultado sea texto

numero2 = 4.4
print (numero + numero2)
#nota: tambien se pueden sumar variables de distintas formas de datos, pero tienen que pertenecer a la misma categoria

