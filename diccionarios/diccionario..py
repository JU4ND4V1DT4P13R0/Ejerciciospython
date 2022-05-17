lista1=[]
lista2=[]

for usuario in range(10):
    usuario=int(input('dijite 10 elementos'))
if usuario%2 == 0:
    lista1.append(usuario)
else:
    lista2.append(usuario)
print(lista1)
print(lista2)