# coding: utf-8
# uma variação do método noves fora


def ordena_lista(lista):
	for i in range(len(lista)-1, 0, -1):
		if lista[i] > lista[i - 1]:
			lista[i], lista[i - 1] = lista[i - 1], lista[i]

def noves_fora(lista):
	saida = []
	saida.append(lista + [])
	l1 = lista + []
	
	while len(l1) != 1:
		soma = l1.pop(0) + l1.pop(0)
		
		while soma >= 9:
			soma -= 9
		l1.append(soma)
		ordena_lista(l1)
		saida.append(l1 + [])
		
	if l1[0] >= 9:
		l1[0] -= 9
		saida.append(l1 + [])
	
	return (l1[0], saida)
	
assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1], 
                                             [7, 5, 4, 3, 1], 
                                             [4, 3, 3, 1], 
                                             [7, 3, 1], 
                                             [1, 1], 
                                             [2]])
assert noves_fora([9]) == (0, [[9], [0]])
