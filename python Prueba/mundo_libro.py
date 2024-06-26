import mantenedor_de_categoria, reportes


while True:
  print("****************************")
  print("*       MUNDO LIBRO         *")
  print("****************************")
  print("""
      [1] - mantenedor de categorias
      [2] - reportes
      [3] - salir      """)
  opcion= int(input("ingrese opcion"))

  if opcion == 1:
    mantenedor_de_categoria.menu_categorias()

  elif opcion == 2:
