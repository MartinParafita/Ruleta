import random

print('Ruleta')

inicio = 0
fin = 37
num_salidos = []

def LANZABOLA(inicio, fin):
    numero = random.randrange(inicio, fin)
    num_salidos.append(numero)
    return numero

def ANALISIS():
    num_norep = set(num_salidos)
    #print(num_norep)
    for i in num_norep:
        repetido = num_salidos.count(i)
        print(f"El numero {i} se repite {repetido}")
    return num_norep


if __name__ == '__main__':
    while len(num_salidos)<100:
        LANZABOLA(inicio,fin)
    print(num_salidos)
    ANALISIS()
    
    
    

    