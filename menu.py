"""" este es el menu principal donde cargamos los archivos, se escoge el tipo de usuario o se sale del sistema"""
import csv, json
import invitado as inv
import administrador as adm
import operador as ope
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
    print("="*45)
    print("Bienvenido al sistema de monitoreo de clima")
    print("="*45)
    print("\n1.registrado  2.visitante  3.salir ")
    tipo_usuario = input("\nIngrese su tipo de usuario:")
    T = True
    while T:
        if tipo_usuario == "1":
            if login():
                T = False
        elif tipo_usuario == "2":
            inv.menu_invitado()
        elif tipo_usuario == "3":
            print("Saliendo del sistema...")
            T = False
        else:
            print("Opción inválida. Por favor, ingrese 'registrado', 'visitante' o 'salir'.")
            tipo_usuario = input("Ingrese su tipo de usuario (registrado, visitante) o 'salir' para salir del sistema: ")
            
    
def login():
    #si es usuario registrado, pide su documento y contraseña para autentificar 
    B = True
    C = True
    while B:
        
            documento = input("\nIngrese su documento:")
            if documento.isdigit():
                break
            print("Numero invalido, por favor vuelva a ingresar su documento")
            
    while C:        
        
            contraseña = input("\nIngrese su contraseña:")
            if contraseña.isdigit():
                break
            print("Numero invalido, por favor vuelva a ingresar su contraseña")
            
    for usuario in usuarios:
        if usuario["codigo"] == documento and usuario["clave"] == contraseña:
            print ("\n", "="*4, "Bienvenido", usuario["nombre"], "su rol es", usuario["rol"], "="*4 )
            if usuario["rol"] == "Operador":
                ope.seleccionar_estacion()
                estacion = input("\nIngrese el número de la estación que desea seleccionar: ")
                print("Escoja que quiere realizar"
                      "\n1. Ver medidas de la estacion"
                      "\n2. Ingresar nuevas medidas")
                accion = input("\nIngrese el número de la acción que desea realizar: ")
                if accion == "1":
                    ope.mostrar_medidas()
                            
            return True

            
    else:
        print("Usuario o contraseña incorrectos")
    return False
    
    # y ver si es operador o administrador
menu_inicial()
