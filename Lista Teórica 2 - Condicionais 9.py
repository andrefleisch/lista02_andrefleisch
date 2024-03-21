idade = int(input("Digite a sua idade: "))
tempoServico = int(input("Digite seu tempo de serviço em anos: "))
if idade >= 65 or tempoServico >= 30 or idade >= 60 and tempoServico >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")    