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
            pais = input("Ingrese Pais ")
            Pais= pais.lower()
            ciudad = input("Ingrese Nombre de Ciudad ")
            Ciudad = ciudad.lower()
            Codigo_postal = input("Ingrese el codigo postal:  ")
            if Ciudades.get(Codigo_postal,None)== None:
                Ciudades[Codigo_postal]={}
                info_ciudad = {
                    "Nombre":Ciudad,
                    "Poblacion": int(input("Ingrese el Nueva Poblacion")),
                    "Pais":Pais
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
                Pais= pais.lower()
                ciudad = input("Ingrese Nombre de Ciudad nuevo")
                Ciudad = ciudad.lower()
                Ciudades[Codigo_postal]["Nombre"] = Ciudad
                Ciudades[Codigo_postal]["Poblacion"] = int(input("Ingrese el Nueva Poblacion"))
                Ciudades[Codigo_postal]["Pais"] = Pais
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


        


def Ver_por_pais():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                                Ver Por Pais
                    ***********************************
                    """)
            pais = input("Pais a Buscar:   ")
            Pais= pais.lower()
            for llave, valor in Ciudades.items():
                if valor.get("Pais") == Pais:
                    print(f"""
                        Ciudad: {valor.get("Nombre")}

                        Codigo Postal: {llave}
                        Pais: {valor.get("Pais")}
                        Poblacion: {valor.get("Poblacion")}
                        """)
            
                else:
                    print("No registra")
            return
        except Exception as e:
            print(f"Error Causado por {e}")


def Ver_por_Ciudad():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                                Ver Por Ciudad
                    ***********************************
                    """)
            ciudad = input("Ingrese el  Nombre de la ciudad:  ")
            Ciudad = ciudad.lower()
            for llave, valor in Ciudades.items():
                if valor.get("Nombre") == Ciudad:
                    print(f"""
                        Ciudad: {valor.get("Nombre")}

                        Codigo Postal: {llave}
                        Pais: {valor.get("Pais")}
                        Poblacion: {valor.get("Poblacion")}
                        """)
                else:
                    print("No registra")
            return
                    
        except Exception as e:
            print(f"Error Causado por {e}")

def Ver_por_Codepostale():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                                Ver Por Codigo
                    ***********************************
                    """)
            Codigo_postal = input("Ingrese el codigo postal:  ")
            for llave, valor in Ciudades.items():
                if llave == Codigo_postal:
                    print(f"""
                        Ciudad: {valor.get("Nombre")}

                        Codigo Postal: {llave}
                        Pais: {valor.get("Pais")}
                        Poblacion: {valor.get("Poblacion")}
                        """)
                else:
                    print("No registra")
            return
                    
        except Exception as e:
            print(f"Error Causado por {e}")


def Buscar_por_Poblacion():
    while True:
        try:
            cargar_datos(Ruta_JSON_Ciudades, Ciudades)
            print("""
                    ***********************************
                            Ver Por Poblacion
                    ***********************************
                    """)
            print("""
                    1. Para menores a un millon
                    2. Para menores de 10 millones pero mayores a un millon
                    3. Para Mayores de 10 millones
                    """)
            info = input("Ingrese el numeor deseado:  ")
            if info == "1":
                for llave, valor in Ciudades.items():
                    if valor.get("Poblacion") <= 1000000:

                        print(f"""
                            Ciudad: {valor.get("Nombre")}

                            Codigo Postal: {llave}
                            Pais: {valor.get("Pais")}
                            Poblacion: {valor.get("Poblacion")}
                            """)
            if info == "2":
                for llave, valor in Ciudades.items():
                    if valor.get("Poblacion") <= 10000000 and valor.get("Poblacion") >=1000000:
                        print(f"""
                            Ciudad: {valor.get("Nombre")}

                            Codigo Postal: {llave}
                            Pais: {valor.get("Pais")}
                            Poblacion: {valor.get("Poblacion")}
                            """)
            if info == "3":
                for llave, valor in Ciudades.items():
                    if valor.get("Poblacion") >= 10000000:

                        print(f"""
                            Ciudad: {valor.get("Nombre")}

                            Codigo Postal: {llave}
                            Pais: {valor.get("Pais")}
                            Poblacion: {valor.get("Poblacion")}
                            """)
            return
            
            
                    
        except Exception as e:
            print(f"Error Causado por {e}")

