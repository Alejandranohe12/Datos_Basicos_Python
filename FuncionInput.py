"""Funcion input para procesar la entrada del usuario
Con input le decimos al usuario que nos de un valor
"""
#ejemplo:
Resultado = input("Escribe un mensaje: ") #la funcion input regresa con un tipo String(str)
print("El valor proporcionado por el usuario es: ", Resultado)
print("Fin del programa")
#Ejemplo2: Aquí realizamos la suma de dos valores que vamos a solicitar al usuario
Numero1 = int(input("escribe el primer numero:")) #colocamos el int para que no sea tipo str, que sea int
Numero2 = int(input("Escriba el segundo numero: "))
resultado = Numero1 + Numero2
print("El resultado de la suma es:", resultado)

#Ejercicio para practicar:
#Califica tu dia del 1 al 10
"""Resultado---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->
---------------------------------------------->

"""
Pregunta = int(input("Cómo estuvo tu día del 1 al 10?: "))
print("Mi día estuvo como un: ", Pregunta)
