def morral(tamanio, pesos, valores, n):
    if n == 0 or tamanio == 0:
        return 0
    
    if pesos[n - 1] > tamanio:
        return morral(tamanio, pesos, valores, n -1)

    return max(valores[n-1] + morral(tamanio - pesos[n-1], pesos, valores, n-1), morral(tamanio, pesos,valores, n-1))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamanio = 25
    n = len(valores)
    

    resultado = morral(tamanio, pesos, valores, n)
    print(resultado)