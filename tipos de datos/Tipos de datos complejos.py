#Un dato complejo es un dato, que tiene multiples datos en si mismo
     #de modo que un solo dato, NO hace un dato complejo
#Para poder crear un dato complejo hay que iniciarlo con "brakets" [] 

lista = ["hola como va todo", 12, True] 
print (lista)
#Esto nos permite agrupar multiples datos en uno solo, independientemente de su tipo

#Supongamos que queremos obtener un dato especifico de la lista, bueno, para eso hay que decirle al programa cual dato queremos recuperar

print (lista[0]) #En este caso, el primer dato de la lista (0) "hola como va todo", va a ser el que nos devuelva, ya que contamos en un ordem de 0, 1, 2... hasta el 9
#si quisieramos obtener el segundo dato, solo tendriamos que cambiar el 0 por un 1

print (lista[1]) #Algo asi
print (lista[5]) #Si nosotros le pidieramos un dato que no existe, nos devolvera un error, ya que no hay un dato en la posicion 5 "IndexError: list index out of range"

#Tambien se pueden hcaer listas utilzando el termino "tupla" (hay que utilizar parentesis en lugar de brakets)

tupla = ("hola como va todo", 12, True)
print (tupla[0])

#Entonces, para que chuchas querriamos utilizar tupla o lista?
#Bueno, la diferencia recae en que una Tupla es un lista de datos que NO se pueden modificar, mientras que una lista si se puede modificar

lista = ["hola como va todo", 12, True]
lista[0] = "hola como va todo, hombre sabroso?"
print (lista[0]) #Aqui la lista actualizo el dato de la posicion 0, le agrego "hombre sabroso?

#Pero si quisieramos hacer lo mismo con Tupla (recordar que hay que utilizar parentesis en lugar de brakets)
tupla = ("hola como va todo", 12, True)
tupla[0] = "hola como va todo, hombre sabroso?"
print (tupla[0]) #Nos devolvera un error, ya que las tuplas NO se actualizan (termino que le das, termino que se queda de por vida por pringao)

#Eso hace que se parezcan en cierto punto a los conjuntos
    #Un conjunto es tambien una forma de agrupar datos, pero que no tienen un orden en especifico
    #Y al igual que las tuplas, tampoco pueden ser modificados (los datos como tal, el orden si)
    
conjunto = {"hola como va todo", 12, True} #hay que reocordar que los conjuntos se hacen con llaves
print (conjunto)
#Los conjuntos son particularmente utiles cuando tenemos datos que no se pueden repetir, ya que si se repiten, el conjunto solo tomara uno de ellos

conjunto = {"hola como va todo", 12, True, "hola como va todo", 12, True}
print (conjunto) #Aqui, el conjunto solo tomara un "hola como va todo", un 12 y un True, ya que los otros dos se repiten (eres grande drake)
#Lo que pasa, es que como no tienen un orden en especifico, no se puede acceder a un dato en especifico, ya que no se sabe cual es cual

print (conjunto[0]) #Nos da error: "TypeError: 'set' object is not subscriptable"(basicamente que estas bien wey eso es un conjunto, no puedes acceder a un dato como si fuera una lista, tienes que hacerlo con un bucle. Despues lo veremos :D)

#Por ultimo, tenemos los diccionarios
    #Estos son igual a las listas, pero en lugar de tener un valor numerico(un orden dentro de la lista) tienen un valor de texto (una clave)

#Los diccionarios se abren con corchetes, y para tener otro valor, se utiliza la coma
diccionario ={
    "nombre" : "ivanosaurio",
    "edad" : 76,
    "vivo" : True, #si estoy vivo (ya se, cine)
    "amante_de_la_vida" : False, #Esto es solo un ejemplo... o no
    "calificacion_de_nalga" : 7.89
}

print (diccionario) #Esto nos va a mostrar todos los datos del diccionario
print (diccionario["vivo"]) #Esto nos va a mostrar el valor de "vivo" que es True, porque pues, sigo vivo
#Para buscar cosas en el diccionario se debe utilizar el termino que ingresamos, no el orden en el que lo pusimos