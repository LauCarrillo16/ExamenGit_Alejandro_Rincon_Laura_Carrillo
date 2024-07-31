from Desarrollo import *

def menuPrincipal():
    while True:
        print("********************************")
        print("Menu Principal")
        print("********************************")
        print("1. Registrar Ciudad")
        print("2. Editar Ciudad")
        print("3. Consultar Ciudad")
        print("4. Salir")
        try:
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                Registro_dict()
            elif opcion == "2":
                Modificar_Datos()
            elif opcion == "3":
                menuMostrar()        
            elif opcion == "4":
                print("Saliendo del Programa")
                break
        except Exception as e:
            print("Opcion invalida")
            

def menuMostrar():
    while True:
        print("********************************")
        print("Menu Mostrar Ciudad")
        print("********************************")
        print("1. Mostrar Todas las Ciudades")
        print("2. Mostrar Ciudades por Nombre")
        print("3. Mostrar Ciudades por Poblacion")
        print("4. Mostrar Ciudades por Pais")
        print("5. Mostrar Ciudades por Codigo Postal")
        print("6. Volver al Menu Principal")
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                Ver_Todas_las_Ciudades()
            elif opcion == 2:
                Ver_por_Ciudad()
            elif opcion == 3:
                ()
            elif opcion == 4:
                Ver_por_pais()
            elif opcion == 5:
                Ver_por_Codepostale()
            elif opcion == 6:
                print("Volver al Menu Principal")
                menuPrincipal()
        except Exception as e:
            print("Opcion invalida")

