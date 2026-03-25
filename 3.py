n1=float(input("Qual foi a primeira nota: "))
n2=float(input("Qual foi a segunda nota: "))
n3=float(input("Qual foi a terceira nota: "))
media=(n1+n2+n3)/2
if media>=7.0 and not media>10:
    print("Você passou.")
elif media<3:
    print("Você foi reprovado.")
elif media>10:
    print("Como?????")
else:
    print("Está de recuperação.")