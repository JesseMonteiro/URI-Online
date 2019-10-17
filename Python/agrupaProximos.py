# Jesse Monteiro Ferreira
# 118210282
# Unidade 6
# Agrupa Proximos


def agrupa_proximos(lista, valor, criterio):
    lista2 = []
    for i in range(len(lista)):
        if ( int (lista[i]) > (valor - criterio)) and ( int (lista[i]) < (valor + criterio)):
                
            lista2.append(lista[i])
            
    return lista2


# l = [1,2,3,4,8,22,3,5]
# print agrupa_proximos(l,4,2)
