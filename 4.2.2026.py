"""
sirka = int(input("Zadejte šířku hřiště: "))
delka=int(input("Zadejte délku hřitě: "))
kola = int(input("Zadejte počet kol: "))
jednoKolo=2*(sirka+delka)
celkoveUbehnu=jednoKolo*kola
print(f"Šířka hřiště je {sirka} metrů a délka je {delka} metrů")
print(f"Jedno kolo má {jednoKolo} metrů")
print(f"Po {kola} kolech uběhnu {celkoveUbehnu} metrů")

"""

# cena=int(input("zadej cenu: "))
# sleva=int(input("sleva v %: "))
# cenaFinal= (cena / 100)* (100 - sleva)
# cenaBefore= (cenaFinal / (100-sleva))*100
# print("cena po sleve: ", cenaFinal)
# print("cena pred slevou: ", cenaBefore)


cislo = int(input("zadejte cislo: "))

if cislo<10:
    cifra=1
elif cislo<100:
    cifra=2
elif cislo<1000:
    cifra=3
elif cislo<1000:
    cifra=4
elif cislo<10000:
    cifra=5
elif cislo<100000:
    cifra=6
else:
    cifra=9999999999
print("cislo je ",cifra," ciferne")



kyclus = 1
cyfra=1
while (cislo>1):
    cyfra+=1
    cislo/=10
print(f"cislo je {cyfra} ciferne")
