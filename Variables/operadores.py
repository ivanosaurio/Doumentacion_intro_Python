#Operador "del" 
# sirve para quitar una variable de nuestro codigo
hola = "saludos gente"
del hola
print (hola)
#esto nos va a dar un error en la terminal
     #"NameError: name 'hola' is not defined"
#del, se utiliza para borrar datos basicamente
#pero supongamos que nosotros tenemos multiples variables
inicio = "Hola como estas "
nombre = f"{inicio} paco master"
print (nombre) #Hola como estas Paco tu padrote
#y nosotros decidimos borrar la variable "inicio"
del inicio
#bueno, lo que pasa es que como nosotros borramos la funcion despues de mostrarala,el valor de dicha funcion fue actualizado antes de que nosotros lo hayamos borrado (hay que recordar que python es un lenguaje que funciona linea por linea, de modo que tiene mayor jerarquia el codigo que esta mas arriba)
#si quisieramos que la funcion fuera borrada, tendriamos que actualizar 
inicio = "Hola como estas"
del inicio
nombre = f"{inicio} paco master"
print (nombre) #sucede que nos dice que la variable "inicio" no esta definida (obviamente porque nosotros la borramos)


#Operador de in/not in 
# sirve para ver si existe algun valor dentro de una variable o no
inicio = "Hola como estas"
print ("como" in inicio) # lo que nos va decir la terminal es 
#"true" ya que como tal el termino que buscamos en la variable "inicio" fue "como", y "como" si esta dentro de la variable, ya que es la definicion de la misma
#ahora, si nosotros quisieramos saber si un termino NO esta dentro de una variable, seria lo mismo exactamente
inicio = "Hola como estas"
print ("como" not in inicio) #Aqui, lo que nos va a decir la terminal es "false", ya que es facdlso que no esta el termino "como" en la variable "inicio"(osea que si esta)
     #nota: es importante tener en cuenta las mayusuculas y minusculas, ya que Python, es un lenguaje sensible (osea que no son terminos distintos para Python: Hola, hola. Y actuara en base a ello)

#Operadores aritmeticos:

#suma y resta (+ y -)
suma = 12 + 5
resta = 12 - 5
multiplicacion = 12 * 5
division = 12 / 5 #devuelve un dato float (flotante)
exponente = 12 ** 5 #potenciaciòn (exponente) (**)
division_baja = 12 // 5 #devuelve entero redondeado hacia abajo
resto = 12 % 5 #devuelve el resto de la division (numero entero)
tipo_de_dato = type(division_baja) #type(dato) nos devuelve que tipo de dato es

#Como se puede ver todos los operadores aritmeticos sriven para ciencias exactas, como las matematicas.

print (suma)
print (resta)
print (multiplicacion)
print (division)
print (exponente)
print (division_baja)
print (resto)
print (tipo_de_dato)

#Estas son las formas en las que podemos hacer operaciones de forma muy sencilla

#Operadores de comparacion
igual_que = 5 == 6 #(==) es para comparar si dos valores son iguales
distinto_de = 5 != 6 #(!=) es para comparar si dos valores son distintos
mayor_que = 5 > 6 # (>) es para comparar si un valor es mayor que otro
menor_que = 5 < 6 # (<) es para comparar si un valor es menor que otro
mayor_o_igual = 5 >= 6 # (>=) es para comparar si un valor es mayor o igual que otro
menor_o_igual = 5 <= 6 # (<=) es para comparar si un valor es menor o igual que otro

#Esto es particularmente para escenarios de practica.
     #Digamos que tenemos un usuario que quiere entrar, y para ello necesitamos de su contraseña (obviamnete)
     #Lo que teneomos que corroborar es que el texto ingresado del usurauio sea igual al de la contraseña que tenemos almacenada en la base de datos
     
contraseña_almacenada ="papusariosabroso12"
contraseña_ingresada = "que onda carnal dejame pasar"
print (contraseña_almacenada == contraseña_ingresada) #nos va a devolver un "false" ya que la contraseña ingresada no es igual a la almacenada
#peeeero, si el usuraio ingresa la contraseña correcta, nos va a devolver un "true"
contraseña_ingresada = "papusariosabroso12"
print (contraseña_almacenada == contraseña_ingresada)

#Tambien sirve para digamos, dar una recompensa en algun videojuego

cantidad_de_puntos = 100
puntos_para_recompensa = 100
print (cantidad_de_puntos >= puntos_para_recompensa) #Esto significa que si el jugador tiene 100 puntos o mas, se le dara una recompensa (ya que es el minimo de punto que se necesita para obtenerla)
  
u = 1 #usuario
ub = 1 #usuario ingresado
c = 2 #contraseñas
cb = 2 #contraseña ingresada

if u == ub: #SI/NO
     if c == cb: #Y
          print ("bienvenido") #entonces
     else: #ingreso cualquier otra cosa (del bloque)
          print ("contraseña erronea") #entonces
elif c == cb: #pero
     print ("usuario no reconocido")#entonces
else: #cualquier otra cosa
     print ("credenciales no reconocidas")

#Operadores Logicos (&/|/not)

#AND
Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso

#OR
Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT
Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True

#Unos operadores que sirven para terminos mateaticos, que en cuenta pueda encontrarles un valor mas util en la practica para humanos promedio con todo gusto lo hare :)