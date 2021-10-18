raw_nk = input()
nk = raw_nk.split()
n = int(nk[0])
k = int(nk[1])

raw_notas = input()
notas = raw_notas.split()#cuidado, este es una cadena de str, hay que realizar casting para hacerlos valores enteros

nota_aprobacion = int(notas[k-1])
notas_int = list(map(lambda x:int(x),notas))

aprobados = [nota for nota in notas_int if nota>=nota_aprobacion]
print(len(aprobados)) #esta linea muestra los aprobados

#comprobar para el segundo caso del enunciado, aun retorna un valor errado
pasan = []
for valores in  aprobados[-1::-1]: #recorriendo la lista de aprobados al revés
    if valores != 0:
        pasan.append(valores)
print(pasan)
print('total que pasan a siguiente ronda: {}'.format(len(pasan)))
