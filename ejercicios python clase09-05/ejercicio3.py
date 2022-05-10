from multiprocessing.pool import IMapIterator


impar=int(input("dijite un numero impar"))
limite=int(input("ingrese un numero limite"))
suma=0
for impar in range(limite):
    if impar%2!=0:
        suma+= impar
        print(impar)
print("la suma de los numeros es:",suma)