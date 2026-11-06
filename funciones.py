def base_datos(usuarios,registros,estaciones):
    #abre todas las bases de datos
    # las carga en las variables del programa
    pass
def menu_inicial():
    #da a elegir tipo de usuario (registrado, visitante) y salir de sistema
     
    pass
def login():
    #si es usuario registrado, pide su documento y contraseña para autentificar 
    # y ver si es operador o administrador
    pass
def menu_operador(estacion):
    #argumento : estacion
    #depende de la estacion pide al usuario
    # si quiere ver todas las medidas o ingresar nuevas medidas
    pass
def mostrar_medidas(inicio_periodo):
    #argumento : inicio_periodo
    #muestra todos los valores registrados segun la estacion
    pass
def ingresar_medidas():
    #ingresa nuevas medidas registradas para la estacion
    #esta toma la fecha y la hora de forma automatica
    pass

def menu_administrador():
    #gestiona estaciones, usuarios y depura
    pass
def gestion_estaciones():
    #da la opcion al usuario de crear, editar, eliminar estacion
    pass
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
    pass
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
