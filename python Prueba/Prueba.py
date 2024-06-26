import json

with open('biblioteca.json','r', encoding= 'utf-8') as file:
    leerJson = json.load(file)

def leer_categoria():
    for i in leerJson["categoria"]:
        print (f"""
               categoriaID: {i["categoria"]}
               nombre: {i[nombre]}
               """)
def agregar_categoria(categoriaID,nombre):
    nueva_categoria ={
        "categoriaID":{len("categoriaID")+1},
        "nombre": nombre

    }
    leerJson["categoria"].append(nueva_categoria)


def editar_categoria(categoriaID, nombre):
   categoriaID = int(input("ingrese ID para editar categoria"))
   nombre = input("ingrese nombre para el producto")

   for categoria in leerJson["categoria"]:
      if categoriaID == categoria["categoriaID"]:
          categoria 
          













def menu_categoria():
    while True:
        print("***************************")
        print("*  MANTENEDOR CATEGORIAS   *")
        print("***************************")
        print("""
              [1] - agregar categortia
              [2] - editar categoria
              [3] - eliminar categoria
              [4] - buscar categoria
              [5] - voler """)
        opcion = int(input("ingresa la opcion"))

        if opcion == 1: