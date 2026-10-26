# ACUÑA LUCAS
# PRIMER PARCIAL

# funciones
def ordenar_alumnos(nombre,promedios,cantidad):
    for i in range(cantidad):
        for j in range(cantidad -1):
            if promedios[j] < promedios[j +1]: 
                auxiliar = promedios[j]
                promedios[j] =  promedios[j + 1]
                promedios[j + 1] = auxiliar

                auxiliar = nombre[j]
                nombre[j] = nombre[j +1]
                nombre[j + 1] = auxiliar

    return nombre,promedios

def calcular_promedios(nota1,nota2):
     return (nota1 + nota2) / 2

# inicializa la variable opcion para que el menu pueda funcionar
opcion = 7


# Comienza el bucle del menu
while opcion != 0:
    print("===============NOTA FÁCIL=================")
    print("1-Cargar alumnos.")
    print("2-Mostrar listado.")
    print("3-Mostrar estadsticas.")
    print("4-Ver ranking.")
    print("5-Buscar alumno.")
    print("6-Juegos con un nombre.")
    print("0-Salir.")

    opcion = int(input("Seleccione una opcion: "))

    match opcion:
        case 1:
            
            cantidad = int(input("Ingrese la cantidad de alumnos: "))

            #inicializando listas para almacenar los datos de los alumnos
            nombre = [""] * cantidad
            nota_parcial1 = [0] * cantidad
            nota_parcial2 = [0] * cantidad
            promedios = [0.0] * cantidad

            # Cargando datos de los alumnos
            for i in range(cantidad):
                nombre_alumno = input("Ingrese el nombre del alumno: ")
                nota1 = int(input("Ingrese la nota del primer parcial: "))
                nota2 = int(input("Ingrese la nota del segundo parcial: "))

                promedios_alumnos = calcular_promedios(nota1,nota2)

                nombre[i] = nombre_alumno
                nota_parcial1[i] = nota1
                nota_parcial2[i] = nota2
                promedios[i] = promedios_alumnos


        case 2:
            #Mostrando listado
            print("Listado.")
            print(F"Nombre: {nombre}")
            print(f"Promedio: {promedios}")

        case 3:
            # Suma todos los promedios y calcula el promedio general de los alumnos
            suma = 0
            for i in range(cantidad):
                suma = suma + promedios[i]

            promedio_general = suma / cantidad

            #Inicializa  los valores de mayor y menor para luego compararlos
            mayor = promedios[0]
            menor = promedios[0]

            #incializo las posiciones de los alumnos para luego guardarlas
            posicion_mayor = 0
            posicion_menor = 0

            contador_promocion = 0
            contador_aprueba = 0
            contador_reprueba = 0

            for i in range(cantidad):
                if promedios[i] > mayor:
                    mayor = promedios[i]
                    posicion_menor = i
                if promedios[i] < menor:
                    menor = promedios[i]
                    posicion_menor = i
                if promedios[i] >= 6:
                    contador_promocion += 1
                elif promedios[i] >= 4:
                    contador_aprueba += 1
                else:
                    contador_reprueba += 1


            #Mostrando estadisticas 
            print(f"Promedio general: {promedio_general}")
            
            print(f"Mejor promedio: {mayor}")
            print(f"Alumno: {nombre[posicion_mayor]}")
            
            print(f"Peor promedio: {menor}")
            print(f"Alumno: {nombre[posicion_menor]}")

            print(f"Alumnos que promocionan: {contador_promocion}")
            print(f"Alumnos que aprueban: {contador_aprueba}")
            print(f"Alumnos que desaprueban: {contador_reprueba}")

        case 4:
            # Asignamos las listas a otras variables para luego ordenarlas
            nombres_ordenados =  nombre
            promedios_ordenados = promedios

            nombres_ordenados,promedios_ordenados = ordenar_alumnos(nombres_ordenados,promedios_ordenados,cantidad)
            promedios_ordenados

            print("RANKING DE ALUMNOS")
            for i in range(cantidad):
                print(i+1,nombres_ordenados[i],promedios_ordenados[i])

        case 5:
            # Inicializamos una variable nombre nueva para para luego comparar con la lista existente
            nombre_buscar = input("Ingrese el nombre del alumno que desea buscar: ")
            encontrado = 0
            for i in range(cantidad):
                if nombre[i] == nombre_buscar:
                    print(f"Nombre: ",nombre[i])
                    print(f"Promedio: {promedios[i]}")
                    encontrado = 1
                if encontrado == 0:
                    print("El alumno no existe.")

        case 6:
            # Inicializamos una variable nombre para luego contar sus vocales o invertir sus caracteres
            nombre_juego = input("Ingrese un nombre: ")

            vocales = "aeiouAEIOU"
            contador_vocales = 0
            nombre_invertido = ""

            for i in range(len(nombre_juego)):
                for j in range(len(vocales)):
                    if nombre_juego[i] == vocales[j]:
                        contador_vocales = contador_vocales + 1
                nombre_invertido =  nombre_juego[i] + nombre_invertido
            print(f"Cantidad de vocales: {contador_vocales}")
            print(f"Nombre invertido: {nombre_invertido}")

        case 0:
            print("Saliendo del programa.")

        case _:
            print("Error, vuelva a escribir una opcion.")