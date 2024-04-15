import csv 

def matricula(nombre_alumno, fecha_alumno, genero_alumno, direccion_alumno, telefono_alumno, correo_alumno, nombre_padre, direccion_padre, numero_padre, correo_padre):
    datos = [nombre_alumno, fecha_alumno, genero_alumno, direccion_alumno, telefono_alumno, correo_alumno, nombre_padre, direccion_padre, numero_padre, correo_padre]
    archivo = "base_matricula.csv"
    with open(archivo, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(datos)
    print("Datos exitosamente guardados en ", archivo)

def visualizar_csv(nombre_archivo): 
    print("Lista de alumnos matriculados:")
    with open(nombre_archivo, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

def buscar_en_csv(nombre_archivo, palabra_busqueda):
    print("Resultados de la búsqueda para '{}':".format(palabra_busqueda))
    with open(nombre_archivo, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if palabra_busqueda in row:
                print(row)

print("Sistema de matrícula, colegio xxxxxxxx")
while True:
    print("\n¿Qué desea realizar?")
    print("1. Matricular alumno") 
    print("2. Verificar alumno matriculado") 
    print("3. Salir")
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        print("\nInformación del alumno: ")
        nombre_alumno = input("Nombre completo del estudiante: ")
        fecha_alumno = input("Fecha de nacimiento: ")
        genero_alumno = input("Género: ")
        direccion_alumno = input("Dirección de residencia: ")
        telefono_alumno = input("Número de teléfono: ")
        correo_alumno = input("Correo electrónico: ")
        print("\nInformación del padre o apoderado: ")
        nombre_padre = input("Nombre completo de los padres o tutores: ")
        direccion_padre = input("Dirección de residencia de los padres o tutores: ")
        numero_padre = input("Números de teléfono de contacto de los padres o tutores: ")
        correo_padre = input("Correos electrónicos de los padres o tutores: ")
        matricula(nombre_alumno, fecha_alumno, genero_alumno, direccion_alumno, telefono_alumno, correo_alumno, nombre_padre, direccion_padre, numero_padre, correo_padre)
    elif opcion == 2:
        print("\n¿Qué desea hacer?")
        print("1. Ver la lista completa de alumnos")
        print("2. Buscar por palabra clave")
        opcion_visualizar = int(input("Ingrese su opción: "))
        
        if opcion_visualizar == 1:
            visualizar_csv("base_matricula.csv")
        elif opcion_visualizar == 2:
            palabra_busqueda = input("Ingrese la palabra que desea buscar: ")
            buscar_en_csv("base_matricula.csv", palabra_busqueda)
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    