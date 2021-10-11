n = int(input())
def problemas():
    total_problemas = 0
    for problemas in range(n):
        raw_solucion = input().split()
        petya = int(raw_solucion[0])
        vasya = int(raw_solucion[1])
        tonya = int(raw_solucion[2])
        decision = petya+vasya+tonya
        if decision >=2:
            total_problemas +=1
    #return total_problemas
    print(total_problemas)

problemas()