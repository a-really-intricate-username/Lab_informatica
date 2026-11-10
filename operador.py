
def seleccionar_estacion():
    #da la opcion al operador de escoger una estacion para ver sus medidas o ingresar nuevas medidas
    print("Seleccione una estación para ver sus medidas o ingresar nuevas medidas:")
    print("\n1. I.E. Concejo Municipal de Itagüí\n",
    "2. E.U. Joaquín Aristizábal\n",
    "3. Hospital\n",
    "4. Torre Social\n",
    "5. Parque principal")
    
def mostrar_medidas():
    estacion = registros["1"]
    
    for categoria, fechas in estacion.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")
    
    estacion = registros["2"]

    for categoria, fechas in estacion.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")

    estacion = registros["3"]

    for categoria, fechas in estacion.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")

    estacion = registros["4"]

    for categoria, fechas in estacion.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")

    estacion = registros["5"]

    for categoria, fechas in estacion.items():
        print(f"\n{categoria}")
        print("Fecha       | Mediciones")
        print("-" * 50)

        for fecha, valores in fechas.items():
            print(f"{fecha} | {valores}")
    
def ingresar_medidas():
    #ingresa nuevas medidas registradas para la estacion
    #esta toma la fecha y la hora de forma automatica
    pass