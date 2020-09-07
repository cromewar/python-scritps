import random


def ordenamiento_burbuja(lista):
    '''
        funcion devuelve la lista ordenada
        input lista list
        returns lista ordenada 
    '''
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n**2) Crecimiento polinominial (no es tan bueno)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista
            
    
    

if __name__ == '__main__':
    tamanio_lista = int(input('tamaño de lista: '))
    # crea una lista de numero randomicos dentro del tamaño determinado por tamanio_lista
    lista = [random.randint(0,100) for i in range(tamanio_lista)]
    print(lista)
    
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
    