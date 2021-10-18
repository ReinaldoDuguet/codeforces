raw_nk = input()
nk = raw_nk.split()
n = int(nk[0])
k = int(nk[1])

raw_notas = input()
notas = raw_notas.split()
nota_aprobacion = int(notas[k-1])
notas_int = list(map(lambda x:int(x),notas))
pasan = []
aprobados = [nota for nota in notas_int if nota>=nota_aprobacion]
for valores in  aprobados[-1::-1]:
    if valores != 0:
        pasan.append(valores)
print(len(pasan))
