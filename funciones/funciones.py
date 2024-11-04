# Definimos una función suma
def suma(x, y):
    resultado = x + y
    return resultado

def resta(a,b):
    res = a - b
    return res

def multiplicacion(k, z):
    resultado = k * z
    return resultado


# Esto es una función que nos calcula el siguiente
def siguiente(numero):
    numero = numero + 1
    return numero



def mayor_de_dos(x, y):
    if(x > y):
        return x
    else:
        return y

def mayor_de_tres(a, b, c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c

def mayor_de_tres2(f, g, h):
    if(f > g) and (f > h):
        return f
    if(g > f) and (g > h):
        return g
    if(h>g) and (h>f):
        return h


def mayor_de_tres3(x, y, z):
   return mayor_de_dos(mayor_de_dos(x, y), z)


def mayor_de_cuatro(v1,v2,v3,v4):
    return mayor_de_tres(mayor_de_dos(v1,v2), v3, v4)

print(mayor_de_cuatro(1,4,10,14))

#print(mayor_de_tres3(10,11,14))
'''
print(mayor_de_tres2(10,11,14))
print(mayor_de_tres2(10,18,14))
print(mayor_de_tres2(20,18,14))
'''
#print("El resultado de la suma es: ", suma(4,5))
#print("El resultado de la multiplicacion es ", multiplicacion(8,5))ç
#print(siguiente(10))

#print(mayor_de_dos(10,8))