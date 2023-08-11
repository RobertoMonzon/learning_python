import os
import pathlib

mi_ruta=pathlib.Path(pathlib.Path.home(),('Recetas'))

def contar_recetas(ruta):
    contador=0
    for txt in pathlib.Path(ruta).glob("**/*.txt"):
        contador+=1
    return contador

def inicio():
    os.system('cls')
    print("*"*50)
    print("Bienvenido al administrador de recetas")
    print("*"*50)
    print("\n")
    print(f"las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas:{contar_recetas(mi_ruta)}")
    eleccion_menu="x"

    while not eleccion_menu.isnumeric() or eleccion_menu not in range(1,7):
        print("Elige una opcion: ")
        print("\n")
        print("""
        [1] - Leer  receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        """)
        eleccion_menu=input()
    return eleccion_menu 

def mostrar_categorias(ruta):
    print("Categorias: ")
    rutas_categorias = pathlib.Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in rutas_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}]- {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1

def elegir_categoria(lista):

    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta=input("\nElige una categoria: ")
    return lista[int(eleccion_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas= pathlib.Path(ruta)
    listas_recetas= []
    contador= 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}]- {receta_str}")
        listas_recetas.append(receta)
        contador +=1
    return listas_recetas


def elegir_recetas(lista):
    eleccion_receta="x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista)+1):
        eleccion_receta=input("\nElije una receta: ")
    return lista[int(elegir_recetas)-1]

def leer_receta(receta):
    print(pathlib.Path.read_text(receta))

def crear_receta(ruta):
    existe= False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta=input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta= input()
        ruta_nueva= pathlib.Path(ruta,nombre_receta)

        if not os.path.exists(ruta_nueva):
            pathlib.Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe=True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe= False

    while not existe:
        print("Escribe el nombre de tu categoria: ")
        nombre_categoria=input()
        print("Escribe tu nueva categoria: ")
        contenido_receta= input()
        ruta_nueva= pathlib.Path(ruta,nombre_categoria)

        if not os.path.exists(ruta_nueva):
            pathlib.Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe=True
        else:
            print("Lo siento, esa categoria ya existe")


def eliminar_receta(receta):
    pathlib.Path.unlink()
    print(f" la receta {receta.name} ha sido eliminada")

def elimar_categoria(categoria):
    pathlib.Path(categoria).rmdir()
    print(f"la categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar="x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar= input("\n Presione V para volver al menu")

finalizar_programa= False
while not finalizar_programa:
    menu=inicio()

    if menu== 1:
        mis_categorias= mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_categorias)
        mis_recetas= mostrar_recetas(mi_categoria)
        mi_receta=elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias= mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_receta(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias= mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_categorias)
        mis_recetas= mostrar_recetas(mi_categoria)
        mi_receta=elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias= mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_categorias)
        elimar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa= True
