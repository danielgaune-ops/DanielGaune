juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate'],
}

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

def stock_plataforma(plataforma, juegos, inventario):
    total_stock = 0
    plat_buscada = plataforma.lower()

    for codigo, datos in juegos.items():
        plat_juego = datos[1].lower()
        if plat_juego == plat_buscada:
            total_stock += inventario[codigo][1]

    print("El total de stock disponible es: {total_stock}")

def busqueda_precio(p_min, p_max, juegos, inventario):
    encontrados = []

    for codigo, datos_inv in inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]

        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            encontrados.append(f"{titulo}--{codigo}")

    if encontrados:
        encontrados.sort()
        print("Los juegos encontrados son:", encontrados)
    else:
        print("No hay juegos en ese rango de precios")

def buscar_codigo(codigo, diccionario):
    return codigo.upper() in diccionario

def actualizar_precio(codigo, nuevo_precio, inventario):
    if buscar_codigo(codigo, inventario):
        inventario[codigo.upper()][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo, juegos):
    if not codigo or codigo.isspace():
        return False
    return not buscar_codigo(codigo, juegos)

def validar_titulo(titulo):
    return bool(titulo and not titulo.isspace())

def validar_plataforma(plataforma):
    return bool(plataforma and not plataforma.isspace())

def validar_genero(genero):
    return bool(genero and not genero.isspace())

def validar_clasificacion(clasificacion):
    return clasificacion in ['E', 'T', 'M']

def validar_multiplayer(multiplayer):
    return multiplayer.lower() in ['s', 'n']

def validar_editor(editor):
    return bool(editor and not editor.isspace())

def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False
    
def validar_stock(stock):
    try:
        return int(stock) >= 0
    except ValueError:
        return False
    
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, juegos):
        return False
    
    es_multi = True if multiplayer.lower() == 's' else False

    juegos[cod_upper] = [titulo, plataforma, genero, clasificacion, es_multi, editor]
    inventario[cod_upper] = [int(precio), int(stock)]
    return True

def eliminar_juego(codigo, juegos, inventario):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, juegos):
        del juegos[cod_upper]
        del inventario[cod_upper]
        return True
    return False

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()

    if opcion == 1:
        plat = input("Ingrese plataforma")
        stock_plataforma(plat, juegos, inventario)
    
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                if p_min >= 0 and p_min <= p_max:
                    break
                else:
                    print("Valores de precio invalidos. El minimo debe se rmenor o igual al maximo.")
            except ValueError:
                print("Debe ingresar valores de precio validos")
        busqueda_precio(p_min, p_max, juegos, inventario)

    elif opcion == 3:
        while True:
            cod = input("Ingerse codigo del juego: ")
            if not buscar_codigo(cod, inventario):
                print("El codigo no existe")
                resp = input("Desea actualizar otro precio (s/n): ")
                if resp.lower() == 'n':
                    break
            else:
                while True:
                    try:
                        nuevo_p = int(input("Ingrese nuevo precio: "))
                        if nuevo_p > 0:
                            break
                        else:
                            print("El precio debe ser mayor a 0")
                    except ValueError:
                        print("Debe ingresar un valor entero")

                if actualizar_precio(cod, nuevo_p, inventario):
                    print("Precio actualizado")
                break

    elif opcion == 4:
        cod = input("Ingrese codigo del juego: ")
        if not validar_codigo(cod, juegos):
            print("Error en codigo: No puede estar vacio y no debe existir previamente.")
            continue

        tit = input("Ingrese titulo: ")
        if not validar_titulo(tit):
            print("Error: Titulo invalido.")
            continue

        plat = input("Ingrese plataforma: ")
        if not validar_plataforma(plat):
            print("Error: Plataforma invalida.")
            continue

        gen = input("Ingrese genero: ")
        if not validar_genero(gen):
            print("Error: Genero invalido.")
            continue

        clas = input("Ingrese clasificacion: ")
        if not validar_clasificacion(clas):
            print("Error: Clasificaion invalida.")
            continue

        mult = input("Ingrese si es multiplayer (s/n): ")
        if not validar_multiplayer(mult):
            print("Error: Opocion multiplayer invalida. Ingrese 's' o 'n'.")
            continue

        edi = input("Ingrese editor: ")
        if not validar_editor(edi):
            print("Error: Editor invalido.")
            continue

        pre = input("Ingrese precio: ")
        if not validar_precio(pre):
            print("Error: Precio invalido. Debe ser entero, mayor o igual a 0.")
            continue

        stk = input("Ingrese stock: ")
        if not validar_stock(stk):
            print("Error: Stock invalido. Debe ser entero, mayor o igual a 0")
            continue

        if agregar_juego(cod, tit, gen, clas, mult, edi, pre, stk, juegos, inventario):
            print("Juego agregado.")
        else:
            print("El codigo ya existe.")

    elif opcion == 5:
        cod = input("Ingrese codigo del juego a eliminar: ")
        if eliminar_juego(cod, juegos, inventario):
            print("Juego eliminado.")
        else:
            print("El codigo no existe.")

    elif opcion == 6:
        print("Programa Finalizado.")
        break                                             
