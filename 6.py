l1=float(input("Diga um lado do triângulo: "))
l2=float(input("Diga outro lado do triângulo: "))
l3=float(input("Diga mais um lado do triângulo: "))
if l1==l2==l3:
    print("Equilatero")
elif l1==l2 or l2==l3 or l3==l1:
    print("Isósceles")
else:
    print("Obtuso")