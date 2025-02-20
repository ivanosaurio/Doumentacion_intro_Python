#Un condicionante es una funcion que nos permite dar un requisito al tprograma para poder ejecutar cierta ´parte del codigo.
#En caso de que se cumpla cierta condicion(if), se ejecutara cierta parte, y en caso de que no (else), se hara otra accion

edad = 23 #Ejemplo con un bloqueo en base a la edad del usuario

if edad >=18:
    print("adelante crack")
else:
    print("Epaaa, quieto ahi tigre!")

#En esta parte hay que tomar en cuenta que todo lo que coloquemos dentro del bloque de codigo, se ejecutara como una sola accion. En caso de que queramos llevar a cabo otra accion, tenemos que salirnnos de ese bloque y empezar otro nuevo

edad = 17
if edad == 18:
    print("Ahhh perrin, eres justo el man que anda el borde de este show") #todo esto
    print("espero que todo este bien") #es parte
    print("y si no pues tremenda f") #del mismo bloque
else:
    print("chale, nos fallaste chuek") #Y esto 
    print("eso te pasa por viejo verde")#Es otro bloque
    
#Ya que tenemos en cuenta estos condicionales, podemos ver unos un poco mas complejos.
#Supongamos que queremos tener multiples condiciones dentro de un programa. No podemos solo usar (else) ya que seria la unica condicion que se ejecutaria, si no que tenemos que usar una "condicion extra" (elif)

edad_del_perro = 1 #Esta es la edad del perro
if edad_del_perro >= 10: #Esta es la primera condicion
    edad_del_perro("tu perro ya esta viejo carnal, hay que despedirse :()")
elif edad_del_perro >= 5: #en caso de que la primera condicion no se cumpla, se ejecutara esta
    print ("Todavia tienes perro para rato amigo")
elif edad_del_perro >= 2: #Y si no esta
    print ("Acaba de iniciar tu carnal, no hay falla pa")
elif edad_del_perro <=1: #Y si no esta :)
    print ("esa weona apenas y sabe donde esta")
    
#Como se puede ver, cada uno de los elif estan en bloques distintos, ya que son indepedientes de la condicion inicial
#Pero supongamos que la condicion inicial tiene multiples requisitos, entonces lo que se puede hacer es poner multiples (if), dentro de otro

donas = "si"
nombres = {
    "nombre 1": "Samantha",
    "nombre 2": "Patricio",
    "nombre 3": "yo"
}
de_quien_es_la_dona = nombres["nombre 3"]

if donas == "si":
    if de_quien_es_la_dona == nombres["nombre 1"]:
            print ("no se puede agarra jefe")
    if de_quien_es_la_dona == nombres["nombre 2"]:
            print ("no se puede agarra jefe")
    if de_quien_es_la_dona == nombres["nombre 3"]:
            print ("a huevo hay donas, me voya chingar una")
else:
    print ("me lleva la cola no hay donas")