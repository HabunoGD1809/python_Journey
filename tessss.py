class Dog:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        print(f"{self.nombre} dice guau")
        
    def mostrarEdad(self):
        print(f"la edad de {self.nombre} es {self.edad}")

mi_perro = Dog('elias', 3)

mi_perro.ladrar()
mi_perro.mostrarEdad()