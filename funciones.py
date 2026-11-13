"""
Este es el archivo de funciones

Aqui se tienen todas las funciones esenciales para el funcionamiento del programa

Estan incluidas las funciones para el trabajo del administrador, operadores y usuarios visitantes

Ademas aqui se tienen cargadas en variables las listas y diccionarios con los registros
de las estaciones, las estaciones en si mismas y los usuarios registrados
"""
import csv, json
from datetime import datetime, timedelta
def base_datos(Archivo_usuarios,Archivo_estaciones,Archivo_registros,Archivo_variables,Archivo_registros_v2):
    #abre todas las bases de datos las lee y las guarda en variables
    #los csv quedan guardados en listas de diccionarios
    global usuarios, estaciones, registros, variables, registros_v2

    with open(Archivo_usuarios, 'r')as archivo_usuarios:
        lector_csv = csv.DictReader(archivo_usuarios, delimiter=',')
        usuarios = list(lector_csv)
    
    with open(Archivo_estaciones, 'r')as archivo_estaciones:
        lector_csv2 = csv.DictReader(archivo_estaciones, delimiter=',')
        estaciones = list(lector_csv2)
    #los json quedan guardados en diccionarios
    with open(Archivo_registros, 'r')as archivo_registros:
        registros = json.load(archivo_registros)
    with open(Archivo_registros_v2, 'r')as archivo_registros:
        registros_v2 = json.load(archivo_registros)

    with open(Archivo_variables, 'r')as archivo_variables:
        variables = json.load(archivo_variables)


# las carga en las variables del programa

def login():
    #si es usuario registrado, pide su documento y contraseña para autenticar
    #y ver si es operador o administrador
    global documento_usuario_activo
    while True:
        documento_valido = False
        while not documento_valido:
            documento = input("\nIngrese su documento ('Salir' para volver):").strip()
            if documento == "Salir":
                return False, None
            elif documento.isdigit() and len(documento) == 10:
                documento_valido = True
            else:
                print("Por favor vuelva a ingresar su documento, (debe ser un número de 10 dígitos)")
        contrasena_valida = False
        while not contrasena_valida:
            contrasena = input("\nIngrese su contraseña:").strip()
            if len(contrasena) == 0:
                print("Por favor ingrese su contraseña")
            else:
                contrasena_valida = True

            

        for usuario in usuarios:
            if usuario["codigo"] == documento and usuario["clave"] == contrasena:
                documento_usuario_activo = documento
                print(f"\n==== Bienvenido {usuario['nombre']}, su rol es {usuario['rol']} ====")
                return True, usuario['rol']
                
        print("Usuario o contraseña incorrectos")

def seleccionar_estacion():
    #da la opcion de escoger una estación para ver sus medidas o ingresar nuevas medidas
    while True:
        print("\nSeleccione una estación para ver sus medidas o ingresar nuevas medidas:")
        print("0. Atrás")
        for estacion in estaciones:
            print(f"{estacion['codigo']}. {estacion['nombre']}")
        estacion_elegida = input("\nIngrese el código de la estación: ").strip()
        if estacion_elegida == "0":
            print("Volviendo al menu inicial")
            return None
        for estacion in estaciones:
            if estacion["codigo"] == estacion_elegida:
                return estacion_elegida
        print("Código de estación inválido. Por favor, intente nuevamente.")
    
def mostrar_medidas(codigo):
    #muestra todas las medidas registradas de la estación
    if codigo not in registros:
        print("Esa estación todavía no tiene un registro en registros.json.")

    estacion_elegida = registros[codigo]

    for categoria, fechas in estacion_elegida.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")

def ingresar_medidas(codigo_estacion):
    #ingresa nuevas medidas registradas para la estacion
    #esta toma la fecha de forma automatica
    # Comprueba que la estación exista en los registros.
    if codigo_estacion not in registros:
        print("Esa estación todavía no tiene un registro en registros.json.")
    # Guarda la fecha actual.
    momento = datetime.now().strftime("%Y-%m-%d")
    datos_ingresados = {}
    # Pide y valida el valor de cada variable.
    for nombre, limites in variables["variables"].items():
        while True:
            entrada = input(f"Ingrese {nombre} ({limites['minimo']} a {limites['maximo']} {limites['unidades']}) o ND: ").strip()

            if entrada.upper() == "ND":
                datos_ingresados[nombre] = -999
                break

            try:
                valor = float(entrada.replace(",", "."))
            except ValueError:
                print("Escriba un número o ND.")
                continue

            if limites["minimo"] <= valor <= limites["maximo"]:
                datos_ingresados[nombre] = valor
                break

            print(f"El valor debe estar entre {limites['minimo']} y {limites['maximo']}.")

    # Añade las medidas a la estación seleccionada
    for nombre, valor in datos_ingresados.items():
        registros[codigo_estacion].setdefault(nombre, {})
        registros[codigo_estacion][nombre][momento] = valor

    # Guarda los cambios en registros.json
    guardar_archivos("registros")

    print("Medidas registradas:", momento)

def gestion_estaciones():
    #da la opcion al usuario de crear, editar, eliminar estacion
    en_gestion_estaciones = True
    while en_gestion_estaciones:

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
            print("Volviendo al menu de administrador")
            en_gestion_estaciones = False
        else:
            print("Por favor ingrese una opcion valida")

def crear_estacion():
    #Toma automaticamente el numero mayor de estacion de la base de datos, pide el nombre al usuario y lo añade al sistema
    global estaciones
    max_codigo = max((int(estacion["codigo"]) for estacion in estaciones), default=0)
    codigo_estacion = str(max_codigo + 1)  
    estacion_valida = False
    while not estacion_valida:
        nombre_estacion = input("Ingrese el nombre para la nueva estacion: ")
        if len(nombre_estacion.strip()) == 0:
            print("No puede ingresar un nombre vacio")
        else:
            estacion_valida = True
    nueva_estacion = {"codigo": codigo_estacion, "nombre": nombre_estacion}
    estaciones.append(nueva_estacion)
    print(f"Estación creada con éxito con el código {codigo_estacion}.")

    guardar_archivos("estaciones")

def editar_estacion():
    #Pide al usuario el codigo de la estacion y le permite modificar su nombre (El codigo se mantiene igual)
    print("Estaciones registradas")
    print("Codigo\t|\tNombre estacion")
    for estacion in estaciones:
        print(estacion['codigo'],'\t'*2,estacion['nombre'])
    encontrado = False
    estacion_valida = False
    while not encontrado:
        codigo_estacion = input("Ingrese el codigo de la estacion que quiere modificar: ")
        while not estacion_valida:
            nombre_estacion = input("Ingrese el nuevo nombre para la estacion: ")
            if len(nombre_estacion.strip()) == 0:
                print("No puede ingresar un nombre vacio")
            else:
                estacion_valida = True
        for estacion in estaciones:
            if estacion["codigo"] == codigo_estacion:  
                estacion["nombre"] = nombre_estacion
                encontrado = True
                print("Estación actualizada con éxito.")
                break

        if not encontrado:
            print("No se encontró ninguna estación con ese código, por favor intentelo nuevamente")
    guardar_archivos("estaciones")

def eliminar_estacion():
    #Pide al usuario el codigo de una estacion y permite eliminarla de la lista de estaciones (siempre y cuando no tenga registros asociados)
    global estaciones
    print("Estaciones registradas")
    print("Codigo\t|\tNombre estacion")
    for estacion in estaciones:
        print(estacion['codigo'],'\t'*2,estacion['nombre'])
    codigo_estacion = input("Ingrese el codigo de la estacion a eliminar: ")
    
    if codigo_estacion in registros and len(registros[codigo_estacion]) > 0:
        print("Error: No se puede eliminar esta estación porque tiene valores o registros asociados.")
    else:
        estaciones = [estacion for estacion in estaciones if estacion["codigo"] != codigo_estacion]
        
        if codigo_estacion in registros:
            del registros[codigo_estacion]
            
        print("Estación eliminada con éxito.")

    guardar_archivos("estaciones")
    guardar_archivos("registros")

def gestion_usuarios():
    #ofrece las opciones de crear un nuevo usuario, editar el usuario y contrasena de una cuenta y eliminar un usuario
    en_gestion_usuarios = True
    while en_gestion_usuarios:
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
            en_gestion_usuarios = False
        else:
            print("Por favor ingrese una opcion valida.")


def crear_usuario():
    #Se ingresa documento, nombre completo, contrasena, confirmacion de la contrasena y el rol del usuario (Administrador u operador)
    Documento_invalido = True
    Contrasena_invalida = True
    Nombre_invalido = True
    Rol_invalido = True
    while Documento_invalido:
        Documento_invalido = False
        Documento = input("Ingrese el numero de documento del nuevo usuario:  ")
        if len(Documento.strip()) != 10 or not Documento.isdigit():
            Documento_invalido = True
            print("Por favor ingrese numero de documento valido")
            continue
        for usuario in usuarios:
            
            if usuario["codigo"] == Documento:
                print("Documento invalido, ya esta en el sistema, intentelo nuevamente")
                Documento_invalido = True
                break
    while Nombre_invalido:
        Nombre_invalido = False
        Nombre = input("Ingrese el nombre para el nuevo usuario:  ")
        if not Nombre.replace(" ", "").isalpha():
            Nombre_invalido = True
            print("Por favor ingrese un nombre valido")
    while Contrasena_invalida:
        Contrasena_invalida = False
        Contrasena1 = input("Ingrese la contraseña para el nuevo usuario:  ")
        Contrasena2 = input("Ingrese la contraseña nuevamente:  ")
        if Contrasena1 != Contrasena2:
            print("Las contraseñas no coinciden, intentelo nuevamente")
            Contrasena_invalida = True
        elif len(Contrasena1) < 4:
            Contrasena_invalida = True
            print("Es necesario que ingrese una contraseña de al menos 4 caracteres, por favor intentelo nuevamente")
    while Rol_invalido:
        Rol_invalido = False
        Rol = input("Ingrese el rol para el nuevo usuario ('Operador' -- 'Administrador')")
        if Rol != "Operador" and Rol != "Administrador":
            Rol_invalido = True
            print("Por favor ingrese un rol valido")
    nuevo_usuario = {'codigo':Documento,'nombre':Nombre,'clave':Contrasena1,'rol':Rol}
    usuarios.append(nuevo_usuario)
    print("Se ha creado el nuevo usuario con exito")
    
    guardar_archivos("usuarios")

def editar_usuario():
    #se puede elegir un usuario del listado y modificar su nombre, contrasena y rol
    print("Usuarios registrados")
    print("Documento\t|\tNombre\t|\tContraseña\t|\tRol")
    for usuario in usuarios:
        print(usuario['codigo'],'\t'*2,usuario['nombre'],'\t',usuario['clave'],'\t'*2,usuario['rol'])
    usuario_invalido = True
    while usuario_invalido:
        Documento_invalido = True
        while Documento_invalido:
            Documento_invalido = False
            Documento = input("Ingrese el numero de documento del nuevo usuario:  ")
            if len(Documento.strip()) != 10 or not Documento.isdigit():
                Documento_invalido = True
                print("Por favor ingrese numero de documento valido")
                continue
        for usuario in usuarios:
            if usuario["codigo"] == Documento:  
                Contrasena_invalida = True
                Nombre_invalido = True
                Rol_invalido = True
                while Nombre_invalido:
                        Nombre_invalido = False
                        Nombre = input("Ingrese el nombre nuevo para el usuario:  ")
                        if not Nombre.replace(" ", "").isalpha():
                            Nombre_invalido = True
                            print("Nombre no valido")
                while Contrasena_invalida:
                    Contrasena_invalida = False
                    Contrasena1 = input("Ingrese la nueva contraseña para el usuario:  ")
                    Contrasena2 = input("Ingrese la contraseña nuevamente:  ")
                    if Contrasena1 != Contrasena2:
                        print("Las contraseñas no coinciden, intentelo nuevamente")
                        Contrasena_invalida = True
                    elif len(Contrasena1) < 4:
                        Contrasena_invalida = True
                        print("Es necesario que ingrese una contraseña de al menos 4 caracteres, por favor intentelo nuevamente")
                while Rol_invalido:
                    Rol_invalido = False
                    Rol = input("Ingrese el rol para el usuario ('Operador' -- 'Administrador')")
                    if Rol != "Operador" and Rol != "Administrador":
                        Rol_invalido = True
                        print("Por favor ingrese un rol valido")
                usuario["nombre"] = Nombre
                usuario["clave"] = Contrasena1
                usuario["rol"] = Rol
                usuario_invalido = False
                print("Usuario actualizado con éxito.")
                break
        if usuario_invalido:
            print('Usuario no encontrado, intentelo nuevamente')
    guardar_archivos("usuarios")

def eliminar_usuario():
    #elige un usuario del listado y lo elimina (no se puede eliminar el usuario actual en el sistema)
    global usuarios
    print("Usuarios registrados")
    print("Documento\t|\tNombre\t|\tContraseña\t|\tRol")
    for usuario in usuarios:
        print(usuario['codigo'],'\t'*2,usuario['nombre'],'\t',usuario['clave'],'\t'*2,usuario['rol'])
    usuario_invalido = True
    Documento_invalido = True
    while usuario_invalido:
        while Documento_invalido:
            Documento_invalido = False
            Documento = input("Ingrese el numero de documento del nuevo usuario:  ")
            if len(Documento.strip()) != 10 or not Documento.isdigit():
                Documento_invalido = True
                print("Por favor ingrese numero de documento valido")
        for usuario in usuarios:
            if usuario["codigo"] == Documento:
                if Documento == documento_usuario_activo:
                    print("Error: No se puede eliminar este usuario porque es el usuario actual del sistema.")
                    Documento_invalido = True
                    continue
                else:
                    usuarios = [usuario for usuario in usuarios if usuario["codigo"] != Documento]
                    print("Usuario eliminado con exito")
                    usuario_invalido = False
                    continue
    guardar_archivos("usuarios")

    
def depuracion():
    #Ofrece opciones de depuracion al administrador, con las opciones de reportar las medidas comunes en los archivos o las que aparecen en cualqiera de los dos
    print("Opciones de depuracion")
    print("1. Registros comunes")
    print("2. Cualquiera de los dos")
    eleccion = input("Ingrese la opcion a depurar:  ")
    if eleccion == "1":
        for registro in registros:
            if registro in registros_v2:
                print(registro,registros[registro])
    elif eleccion == "2":
        for registro in registros:
            print(registro,registros[registro])
        for registro in registros_v2:
            if registro not in registros:
                print(registro,registros_v2[registro])

def pedir_fecha(mensaje):
    #pide una fecha en formato AAAA-MM-DD y la valida; devuelve un date (o None si escribe 0)
    while True:
        entrada = input(mensaje).strip()
        if entrada == "0":
            return None
        try:
            return datetime.strptime(entrada, "%Y-%m-%d").date()
        except ValueError:
            print("Fecha inválida. Use el formato AAAA-MM-DD (ejemplo: 2026-11-13) o 0 para cancelar.")
 
 
def visualizar_estadisticas():
    #el visitante elige periodo, variables y salida; se calcula maximo (con estacion y fecha),
    #minimo (con estacion y fecha) y promedio de cada variable. Los valores -999 (ND) se excluyen
    hoy = datetime.now().date()
 
    # 1. Periodo
    while True:
        print("\nSeleccione el periodo:",
              "\n1. Últimos 7 días",
              "\n2. Últimos 30 días",
              "\n3. Fechas manuales",
              "\n0. Atrás")
        opcion = input("Ingrese una opción: ").strip()
        if opcion == "0":
            return
        elif opcion == "1":
            fecha_inicio, fecha_fin = hoy - timedelta(days=7), hoy
            break
        elif opcion == "2":
            fecha_inicio, fecha_fin = hoy - timedelta(days=30), hoy
            break
        elif opcion == "3":
            fecha_inicio = pedir_fecha("Fecha de inicio (AAAA-MM-DD, 0 para cancelar): ")
            if fecha_inicio is None:
                continue
            fecha_fin = pedir_fecha("Fecha final (AAAA-MM-DD, 0 para cancelar): ")
            if fecha_fin is None:
                continue
            if fecha_inicio > fecha_fin:
                print("La fecha de inicio no puede ser posterior a la fecha final.")
                continue
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
 
    # 2. Variables (una, varias o todas)
    nombres_variables = list(variables["variables"].keys())
    while True:
        print("\nVariables disponibles:")
        for i, nombre in enumerate(nombres_variables, start=1):
            print(f"{i}. {nombre}")
        print("0. Todas")
        entrada = input("Ingrese los números separados por coma (ej: 1,3) o 0 para todas: ").strip()
        if entrada == "0":
            elegidas = nombres_variables
            break
        partes = [parte.strip() for parte in entrada.split(",")]
        if all(p.isdigit() and 1 <= int(p) <= len(nombres_variables) for p in partes):
            indices = sorted({int(p) for p in partes})
            elegidas = [nombres_variables[i - 1] for i in indices]
            break
        print("Selección inválida. Use números de la lista separados por coma.")
 
    # 3. Salida
    while True:
        print("\n¿Cómo desea ver los resultados?",
              "\n1. En pantalla",
              "\n2. Guardarlos en Estadisticas.txt")
        salida = input("Ingrese una opción: ").strip()
        if salida in ("1", "2"):
            break
        print("Opción inválida. Por favor, intente nuevamente.")
 
    # 4. Cálculo (cada variable por separado, usando todas las estaciones)
    lineas = [f"Estadísticas del {fecha_inicio} al {fecha_fin}", "=" * 50]
    for variable in elegidas:
        unidades = variables["variables"][variable]["unidades"]
        maximo = None
        minimo = None
        suma = 0
        cantidad = 0
        for estacion in estaciones:
            mediciones = registros.get(estacion["codigo"], {}).get(variable, {})
            for fecha_texto, valor in mediciones.items():
                if valor == -999:
                    continue
                try:
                    fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
                except ValueError:
                    continue
                if fecha < fecha_inicio or fecha > fecha_fin:
                    continue
                suma += valor
                cantidad += 1
                if maximo is None or valor > maximo[0]:
                    maximo = (valor, estacion["nombre"], fecha_texto)
                if minimo is None or valor < minimo[0]:
                    minimo = (valor, estacion["nombre"], fecha_texto)
 
        lineas.append(f"\n{variable} ({unidades})")
        if cantidad == 0:
            lineas.append("  No hay mediciones válidas en este periodo.")
        else:
            lineas.append(f"  Máximo:   {maximo[0]} - estación {maximo[1]} - {maximo[2]}")
            lineas.append(f"  Mínimo:   {minimo[0]} - estación {minimo[1]} - {minimo[2]}")
            lineas.append(f"  Promedio: {suma / cantidad:.2f} ({cantidad} mediciones)")
 
    # 5. Mostrar o guardar
    texto = "\n".join(lineas)
    if salida == "1":
        print("\n" + texto)
    else:
        with open("Estadisticas.txt", "w", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
        print("Estadísticas guardadas en Estadisticas.txt")

    

def guardar_archivos(tipo):
    if tipo == "usuarios":
        ruta = "base_datos/usuarios.csv"
        datos = usuarios
        campos = ["codigo", "nombre", "clave", "rol"]
        formato = "csv"

    elif tipo == "estaciones":
        ruta = "base_datos/estaciones.csv"
        datos = estaciones
        campos = ["codigo", "nombre"]
        formato = "csv"

    elif tipo == "registros":
        ruta = "base_datos/registros.json"
        datos = registros
        formato = "json"

    elif tipo == "registros_v2":
        ruta = "base_datos/registros_v2.json"
        datos = registros_v2
        formato = "json"

    elif tipo == "variables":
        ruta = "base_datos/variables.json"
        datos = variables
        formato = "json"

    else:
        print("Archivo desconocido.")
        return

    if formato == "csv":
        with open(ruta, "w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos)
    else:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)