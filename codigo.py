import random

fila_1 = random.sample(range(1, 30), 20)

fila_2 = random.sample(range(1, 30), 20)

numerocres1=sorted(fila_1)
numerocres2=sorted(fila_2) 

print(numerocres1)
print(numerocres2)

fila_um = random.sample(range(1, 30), 20)
fila_dois = random.sample(range(1, 30), 20)

fila_um.sort(reverse=False)
fila_dois.sort(reverse=False)

sobrepoe = [i for i in set(fila_um) if i in fila_dois]

print('Fila um:', fila_um)

print('Fila dois:', fila_dois)

print('Numeros repetidos:', sobrepoe)
