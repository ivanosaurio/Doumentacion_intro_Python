#1.- Un programa que encrypte tus palabras pidiendoselas al usuario
texto1 = input("Que quieres encryptar?:")
texto_en = texto1[::-1]
confirmacion1 = input("confirmar?(si/no):")
if confirmacion1 == "si":
        print (texto_en)
        confirmacion2 = input ("volver a la normalidad?(si/no):")
        if confirmacion2 == "si":
            print ("tu texto desencryptado es este:", texto1)
        else:
            print ("tu texto encryptado es este:", texto_en)
else:
    print("ok, no lo hare")
