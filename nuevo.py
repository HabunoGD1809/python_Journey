import random


def encender(estado):
    if estado == 1:
        print('el auto ya esta encendido')
    else:
        print('auto encendido')

encender(0)


miLista = ['h','o','l','a']

longitud = len(miLista)
print(longitud)

# order inverse
miLista.reverse()
print(miLista)

punto = (3, 5)
colores = ('rojo', 'verde', 'azul')

estudiante = {
    'nombre': 'Juan', 
    'edad': 25, 
    'curso': 'Python'
}

print(estudiante['nombre'])


# conjuntos, unicos de valores 
vocales = {
    'a',
    'e',
    'i',
    'o',
    'u'
}

print(vocales)

for i in range(1,10):
    print(i)
    
    
nombres = ['jose','perez','hector','felicia','andres']

for nombre in nombres:
    print(nombre)


contador = 0
randoM = random.randint(0, 200000000)
while contador < randoM:
    print(contador)
    contador+=1

# colores = ["rojo", "verde", "azul"]
# color_aleatorio = random.choice(colores)
# print(color_aleatorio)
