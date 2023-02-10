# material em python para se exercitar
print("Bem vindo à calculadora de média")
nota_1=float(input("Digite a primeira nota"))
nota_2=float(input("Digite a segunda nota"))
media=(nota_1 + nota_2)/2
if media==10:
    print("Aprovado com distinção")
elif media>= 7:
    print("Aprovado")
else:
    print("Reprovado")