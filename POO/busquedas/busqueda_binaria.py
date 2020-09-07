import random

def busqueda_binaria(lista, inicio, fin, objetivo):
    
    if inicio > fin:
        return False
    
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio +1, fin, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, inicio, medio-1, objetivo)
    
        
        


if __name__ == '__main__':
    tamanio_lista = int(input('Cual es el tamaño de la lista: '))
    objetivo = int(input('que número quieres encontrar: '))
    
    lista = sorted([random.randint(0, 100) for i in range(tamanio_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "No esta"} en la lista')
    
    
