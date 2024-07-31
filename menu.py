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
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            Registro_dict()
        elif opcion == "2":
            ()
        elif opcion == "3":
            ()
        elif opcion == "4":
            print("Saliendo del Programa")
            break
        else:
            print("Opcion invalida")
            
