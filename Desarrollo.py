import json

Ciudades = {}

Ruta_JSON_Ciudades = "Ciudades.json"



def guardar_datos(Ruta_JSON, Datos):
    try:
        contenido = json.dumps(Datos, indent=4,  ensure_ascii=False)
        with open(Ruta_JSON, "w", encoding='utf-8') as file:
            file.write(contenido)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos(Ruta_JSON, Datos):
    try:
        with open(Ruta_JSON, mode="r", encoding='utf-8') as archivo:
            Datos.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar Datos {e}")



def Registro_dict():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                        Registro de Ciudad Nueva
                    ***********************************
                    """)
            Codigo_postal = input("Ingrese el codigo postal:  ")
            if Ciudades.get(Codigo_postal,None)== None:
                Ciudades[Codigo_postal]={}
                info_ciudad = {
                    "Nombre":input("Ingrese el Nombre de la Ciudad"),
                    "Poblacion": int(input("Ingrese el Nueva Poblacion")),
                    "Pais":input("Ingrese el Nombre del PAIS")
                }
                Ciudades[Codigo_postal] = info_ciudad
                guardar_datos(Ruta_JSON_Ciudades, Ciudades)
                return
            else:
                print("Codigo Registrado Anteriormente")
        except Exception as e:
            print(f"Error Causado por {e}")



def Modificar_Datos():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                        Modificar Datos de la ciudad
                    ***********************************
                    """)
            
            Codigo_postal = input("Ingrese el codigo postal:  ")
            if Ciudades.get(Codigo_postal,None)!= None:
                pais = input("Ingrese Pais a Corregir")
                ciudad = input("Ingrese Nombre de Ciudad nuevo")
                Ciudades[Codigo_postal]["Nombre"] = ciudad
                Ciudades[Codigo_postal]["Poblacion"] = int(input("Ingrese el Nueva Poblacion"))
                Ciudades[Codigo_postal]["Pais"] = pais
                guardar_datos(Ruta_JSON_Ciudades, Ciudades)
                return
        except Exception as e:
                    print(f"Error Causado por {e}")

def Ver_Todas_las_Ciudades():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                        Ver Todas las Ciudades
                    ***********************************
                    """)
            for llave, valor in Ciudades.items():
                print(f"""
                        Ciudad: {valor.get("Nombre")}

                        Codigo Postal: {llave}
                        Pais: {valor.get("Pais")}
                        Poblacion: {valor.get("Poblacion")}
                        """)
            return
        except Exception as e:
                    print(f"Error Causado por {e}")


