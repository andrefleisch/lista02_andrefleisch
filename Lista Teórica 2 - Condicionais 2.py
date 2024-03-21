a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))



delta = (b**2) - (4*a*c)
print(f"Delta é igual a {delta}")
if delta > 0:
    print("Existem duas raízes reais distintas")
elif delta == 0:
    print("Existem duas raízes iguais")    
elif delta < 0:
    print("Existem duas raízes imaginárias conjugadas")



      




