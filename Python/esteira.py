def distribui_materia_prima(esteira_materia_prima, n):
    lista_esteiras = []
    esteiras = 0

    for listas in range(n):
        lista_esteiras.append([])

    for i in range(len(esteira_materia_prima)):
        lista_esteiras[esteiras].append(esteira_materia_prima[i])
        esteiras += 1

        if esteiras == len(lista_esteiras):
            esteiras = 0

    return lista_esteiras
