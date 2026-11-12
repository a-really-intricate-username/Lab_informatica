"""" este es el menu principal donde cargamos los archivos, se escoge el tipo de usuario o se sale del sistema"""
import csv, json
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

usuarios, estaciones, registros, variables = base_datos('base_datos/usuarios.csv', 'base_datos/estaciones.csv', 'base_datos/registros.json', 'base_datos/variables.json')
def menu_inicial():
    #da a elegir tipo de usuario (registrado, visitante) y salir de sistema
    print("="*45)
    print("Bienvenido al sistema de monitoreo de clima")
    print("="*45)
    
    while True:
        print("\n1.registrado  2.visitante  3.salir ")
        tipo_usuario = input("\nIngrese su tipo de usuario:")
        if tipo_usuario == "1":
            login()
        elif tipo_usuario == "2":
            menu_invitado()
        elif tipo_usuario == "3":
            print("Saliendo del sistema...")
            return
        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
            
            
    
def login():
    #si es usuario registrado, pide su documento y contraseña para autentificar 
    while True:
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
                    estacion_elegida = seleccionar_estacion()
                    if estacion_elegida is None:
                        return
                    print("Escoja que quiere realizar"
                            "\n1. Ver medidas de la estacion"
                            "\n2. Ingresar nuevas medidas")
                    accion = input("\nIngrese el número de la acción que desea realizar: ")
                    if accion == "1":
                        mostrar_medidas(estacion_elegida)
                                
                

                
        else:
            print("Usuario o contraseña incorrectos")

    
    # y ver si es operador o administrador


def seleccionar_estacion():
    #da la opcion al operador de escoger una estacion para ver sus medidas o ingresar nuevas medidas
    print("\nSeleccione una estación para ver sus medidas o ingresar nuevas medidas:")
    print("\n1. I.E. Concejo Municipal de Itagüí\n"
      "2. E.U. Joaquín Aristizábal\n"
      "3. Hospital\n"
      "4. Torre Social\n"
      "5. Parque principal\n"
      "6. C.C Mayorca\n"
      "7. Atras")
    estacion = input("\nIngrese el número de la estación que desea seleccionar:")
    S = True
    print("Has escogido", estacion)
    while S: 
        if estacion in ["1", "2", "3", "4", "5", "6"]:
            break
        elif estacion == "7":
            
            return None
            
        print("Opción inválida. Por favor, ingrese un número del 1 al 7.")
        estacion = input("Ingrese el número de la estación que desea seleccionar: ")

    return estacion
    
def mostrar_medidas(registro):
    estacion_elegida = registros[registro]
    
    for categoria, fechas in estacion_elegida.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")
    seleccionar_estacion()
    
    
def ingresar_medidas():
    #ingresa nuevas medidas registradas para la estacion
    #esta toma la fecha y la hora de forma automatica
    pass

def menu_administrador():
    #gestiona estaciones, usuarios y depura
    print("Menu Administrador",
          "\n1. Gestion de estaciones",
          "\n2. Gestion de usuarios",
          "\n3. Depuracion",
          "\n4. Atras")
    Seleccion = input("Ingrese la opcion requerida: ")
    if Seleccion == "1":
        gestion_estaciones()
    elif Seleccion == "2":
        gestion_usuarios()
    elif Seleccion == "3":
        depuracion()
    elif Seleccion == "4":
        login()

def gestion_estaciones():
    #da la opcion al usuario de crear, editar, eliminar estacion
    print("Menu Gestion de estaciones",
          "\n1. Crear estacion",
          "\n2. Editar estacion",
          "\n3. Eliminar estacion",
          "\n4. Atras")
    Seleccion = input("Ingrese la opcion requerida: ")
    if Seleccion == "1":
        crear_estacion()
    elif Seleccion == "2":
        editar_estacion()
    elif Seleccion == "3":
        eliminar_estacion()
    elif Seleccion == "4":
        menu_administrador()

def crear_estacion():
    #el administrador crea la estacion y su codigo se genera automaticamente
    pass
def editar_estacion():
    #el administrador edita el nombre de la estacion
    #solo se puede cambiar el nombre el codigo es fijo
    pass
def eliminar_estacion():
    #el administrador puede elegir una estacion del listado para eliminarla
    pass
def gestion_usuarios():
    #ofrece las opciones de crear un nuevo usuario, editar el usuario y contrasena de una cuenta y eliminar un usuario
    print("Menu Gestion de usuarios",
          "\n1. Crear usuario",
          "\n2. Editar usuario",
          "\n3. Eliminar usuario",
          "\n4. Atras")
    Seleccion = input("Ingrese la opcion requerida: ")
    if Seleccion == "1":
        crear_usuario()
    elif Seleccion == "2":
        editar_usuario()
    elif Seleccion == "3":
        eliminar_usuario()
    elif Seleccion == "4":
        menu_administrador()

def crear_usuario():
    #Se ingresa documento, nombre completo, contrasena, confirmacion de la contrasena y el rol del usuario (Administrador u operador)

    pass
def editar_usuario():
    #se puede elegir un usuario del listado y modificar su nombre, contrasena y rol
    pass
def eliminar_usuario():
    #elige un usuario del listado y lo elimina (no se puede eliminar el usuario actual en el sistema)
    pass
def depuracion():
    #Ofrece opciones de depuracion al administrador, con las opciones de reportar las medidas comunes en los archivos o las que aparecen en cualqiera de los dos
    pass
def menu_invitado():
    #permite acceder a la opcion de visualizacion de estadisticas
    pass
menu_inicial()
