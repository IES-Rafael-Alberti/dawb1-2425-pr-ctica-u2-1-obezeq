valor = input("> ")

if '.' in valor:
    puntos = valor.split('.')
    if len(puntos) > 2:
        print(False)
    else:
        print(True)