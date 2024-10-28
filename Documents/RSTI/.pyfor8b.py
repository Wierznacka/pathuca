x=0
y=0
inter_ini = int(input("Digite o valor inicial: "))
inter_fim = int(input("Digite valor fim: "))
for i in range(inter_ini, inter_fim):
    numero = int(input("Digite valor:"))
    if numero >= inter_ini and numero <=inter_fim:
     x+=1
    else:
       y+=1
    t(f" {x} entre {inter_ini} e {inter_fim}")
    t(f" {y} fora do intervalo")