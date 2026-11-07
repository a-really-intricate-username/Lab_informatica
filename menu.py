"""" este es el menu principal donde cargamos los archivos, se escoge el tipo de usuario o se sale del sistema"""
import csv, json
import invitado as inv
def base_datos(usuarios,estaciones,registros,variables):
    #abre todas las bases de datos las lee y las guarda en variables
    #los csv quedan guardados en listas de diccionarios
    with open(usuarios, 'r')as archivo_usuarios:
        lector_csv = csv.DictReader(archivo_usuarios, delimiter=',')
        datos_usuarios = list(lector_csv)
    
    with open(estaciones, 'r')as archivo_estaciones:
        lector_csv2 = csv.DictReader(archivo_estaciones, delimiter=',')
        datos_estaciones = list(lector_csv2)
    #los json quedan guardados en diccionarios
    with open(registros, 'r')as archivo_registros:
        datos_registros = json.load(archivo_registros)
        

    with open(variables, 'r')as archivo_variables:
        datos_variables = json.load(archivo_variables)
        

    return datos_usuarios, datos_estaciones, datos_registros, datos_variables

# las carga en las variables del programa

usuarios, estaciones, registros, variables = base_datos('usuarios.csv', 'estaciones.csv', 'registros.json', 'variables.json')
def menu_inicial():
    #da a elegir tipo de usuario (registrado, visitante) y salir de sistema
    print("Bienvenido al sistema de monitoreo de clima")
    print("1.registrado  2.visitante  3.salir ")
    tipo_usuario = input("Ingrese su tipo de usuario:")
    B = True
    while B:
        if tipo_usuario == "1":
            login()
        elif tipo_usuario == "2":
            inv.menu_invitado()
        elif tipo_usuario == "3":
            print("Saliendo del sistema...")
            B = False
        else:
            print("Opción inválida. Por favor, ingrese 'registrado', 'visitante' o 'salir'.")
            tipo_usuario = input("Ingrese su tipo de usuario (registrado, visitante) o 'salir' para salir del sistema: ")
menu_inicial()
            
    
def login():
    #si es usuario registrado, pide su documento y contraseña para autentificar 
    # y ver si es operador o administrador
    pass
