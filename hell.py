import math

def run():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    value = math.pow(base,exponente)
    print(f"valor de {base} elevado a {exponente} es:", int(value))
    
if __name__ == "__main__":
    run()