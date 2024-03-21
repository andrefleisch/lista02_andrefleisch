altura = float(input("Digite a sua altura: "))
sexo = int(input("Digite 1 se você for homem ou 2 se você for mulher: "))
if sexo == 1:
    peso_ideal = (72.7*altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f}")
elif sexo == 2:
    peso_ideal = (62.1*altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f}")



    