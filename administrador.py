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