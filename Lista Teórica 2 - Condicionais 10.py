universidade = int(input("Digite o número de sua universidade 1 - PUC ; 2 - UNICAMP: "))
nota_1 = float(input("Digite a sua primeira nota: "))
nota_2 = float(input("Digite a sua segunda nota: "))
nota = (nota_1 + nota_2) / 2
print(f"Sua nota é {nota}")
if universidade == 1:
    if nota >= 7:
        print("Aprovado")
    elif nota <= 4 < 7:
        print("Em exame") 
    elif nota < 4:
        print("Reprovado")     
elif universidade == 2:
    if nota >= 5:
        print("Aprovado")
    if nota < 5:
        print("Em exame")