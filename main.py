"""
Este es el archivo main

Aqui se tiene los menus principales para el funcionamiento del sistema
"""
import funciones as fun

fun.base_datos('base_datos/usuarios.csv', 'base_datos/estaciones.csv', 'base_datos/registros.json', 'base_datos/variables.json', 'base_datos/registros_v2.json')


while True:
    logged_in = False
    print("="*45)
    print("Bienvenido al sistema de monitoreo de clima")
    print("="*45)
    print("\n1.registrado  2.visitante  3.salir ")
    tipo_usuario = input("\nIngrese su tipo de usuario:").strip()
    if tipo_usuario == "1":
        logged_in = True
        while logged_in:
            logged_in, Rol = fun.login()
            if Rol == "Operador":
                en_menu_operador = True
                estacion_elegida = fun.seleccionar_estacion()
                if estacion_elegida == None:
                    en_menu_operador = False
                    logged_in = False
                while en_menu_operador:
                    print("Escoja qué quiere realizar",
                          "\n1. Ver medidas de la estación",
                          "\n2. Ingresar nuevas medidas",
                          "\n3. Volver al menu inicial")
                    accion = input("\nIngrese el número de la acción que desea realizar: ").strip()
                    if accion == "1":
                        fun.mostrar_medidas(estacion_elegida)
                    elif accion == "2":
                        fun.ingresar_medidas(estacion_elegida)
                    elif accion == "3":
                        confirmacion = input("Esta seguro que quiere volver al menu inicial? \n Esto cerrara su sesion \n Volver al menu inicial ('Si' -- 'No'):   ").lower()
                        if confirmacion == "si":
                            en_menu_operador = False
                            logged_in = False
                        elif confirmacion == "no":
                            pass
                        else:
                            print("Por favor ingrese una opcion valida")
                    else:
                        print("Opción inválida. Por favor, intente nuevamente.")
            elif Rol == "Administrador":
                en_menu_administrador = True
                while en_menu_administrador:
                    print("Menu Administrador",
                          "\n1. Gestion de estaciones",
                          "\n2. Gestion de usuarios",
                          "\n3. Depuracion",
                          "\n4. Atras")
                    Seleccion = input("Ingrese la opcion requerida: ")
                    if Seleccion == "1":
                        fun.gestion_estaciones()
                    elif Seleccion == "2":
                        fun.gestion_usuarios()
                    elif Seleccion == "3":
                        fun.depuracion()
                    elif Seleccion == "4":
                        confirmacion = input("Esta seguro que quiere volver al menu inicial? \n Esto cerrara su sesion \n Volver al menu inicial ('Si' -- 'No'):   ").lower()
                        if confirmacion == "si":
                            en_menu_administrador = False
                            logged_in = False
                        elif confirmacion == "no":
                            pass
                        else:
                            print("Por favor ingrese una opcion valida")
                    else:
                        print("Por favor ingrese una opcion valida")
            
    elif tipo_usuario == "2":
        en_menu_invitado = True
        while en_menu_invitado:
            print("\n==== Menú de visitante ====")
            print("1. Visualizar estadísticas")
            print("0. Volver")
            opcion = input("\nIngrese una opción: ").strip()
            if opcion == "1":
                fun.visualizar_estadisticas()
            elif opcion == "0":
                en_menu_invitado = False
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
    elif tipo_usuario == "3":
        print("Saliendo del sistema...")
        print("Cambios guardados...")
        break
    else:
        print("Opción inválida. Por favor, ingrese 1, 2 o 3.")