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
            "Poblacion":input("Ingrese la poblacion estimada"),
            "Pais":input("Ingrese el Nombre del PAIS")
        }
        Ciudades[Codigo_postal] = info_ciudad
        guardar_datos(Ruta_JSON_Ciudades, Ciudades)


    else:
        print("Codigo Registrado Anteriormente")



Registro_dict()