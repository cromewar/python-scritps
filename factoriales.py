if __name__ == "__main__":
    def factorial(n):
        """
        calcula el facotorial de n
        n int > 0
        returns n!
        """
        if n == 1:
            return 1
        
        return n * factorial(n-1)
    
    n = int(input("Escoje un número: "))
    print(f"El factorial de {n} es {factorial(n)}")
    