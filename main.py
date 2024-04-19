import csv 
from colorama import Fore

def matricula(nombre_alumno,dni, fecha_alumno, genero_alumno, direccion_alumno, telefono_alumno, correo_alumno, nombre_padre, direccion_padre, numero_padre):
    datos = [nombre_alumno, dni, fecha_alumno, genero_alumno, direccion_alumno, telefono_alumno, correo_alumno, nombre_padre, direccion_padre, numero_padre]
    archivo = "base_matricula.csv"
    with open(archivo, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(datos)
    print(Fore.GREEN + "Datos exitosamente guardados en ", archivo)

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
                
def eliminar_alumno(nombre_archivo, dni_eliminar):
    print("Eliminar alumno")
    datos_actualizados = []
    with open(nombre_archivo, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row and row[1] != dni_eliminar:  # Comparando el DNI en la columna 1
                datos_actualizados.append(row)

    with open(nombre_archivo, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(datos_actualizados)

    print(Fore.RED + "Alumno con DNI '{}' eliminado exitosamente del archivo '{}'".format(dni_eliminar, nombre_archivo))




print("Sistema de matrícula, colegio xxxxxxxx")
while True:
    print("\n¿Qué desea realizar?")
    print("1. Matricular alumno") 
    print("2. Verificar alumno matriculado")
    print("3. Eliminar alumno de la Base de Datos")
    print("4. Salir")
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        print("\nInformación del alumno: ")
        nombre_alumno = input("Nombre completo del estudiante: ")
        dni = input("DNI:  ")
        fecha_alumno = input("Fecha de nacimiento: ")
        genero_alumno = input("Género: ")
        direccion_alumno = input("Dirección de residencia: ")
        telefono_alumno = input("Número de teléfono: ")
        correo_alumno = input("Correo electrónico: ")
        print("\nInformación del padre o apoderado: ")
        nombre_padre = input("Nombre completo de los padres o tutores: ")
        direccion_padre = input("Dirección de residencia de los padres o tutores: ")
        numero_padre = input("Números de teléfono de contacto de los padres o tutores: ")
        matricula(nombre_alumno,dni, fecha_alumno, genero_alumno, direccion_alumno, telefono_alumno, correo_alumno, nombre_padre, direccion_padre, numero_padre)
    elif opcion == 2:
        print("\n¿Qué desea hacer?")
        print("1. Ver la lista completa de alumnos")
        print("2. Buscar por palabra clave")
        opcion_visualizar = int(input("Ingrese su opción: "))
        
        if opcion_visualizar == 1:
            visualizar_csv("base_matricula.csv")
        elif opcion_visualizar == 2:
            palabra_busqueda = input("Ingrese el DNI del alumno: ")
            buscar_en_csv("base_matricula.csv", palabra_busqueda)
            
    if opcion == 3 :
        print("Usted desea borrar un alumno de la base de datos")
        palabra_eliminar=  input("Ingrese el número de DNI del alumno que desea eliminar:  ") 
        eliminar_alumno("base_matricula.csv", palabra_eliminar)   
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print(":)")

    