""""
# <87
# <12 50kč
# <18 100kč
# <65 150kč
# foto ano 40kč
povoleni = True

fotka=""
print ("Vstup na horskou dráhu")
print("Zadejte výšku v cm: ")

vyska= input()
# while not isinstance(vyska, int):
#     vyska= input("cislo..")

while type(vyska) != int:
    try:
        vyska = int(vyska)
        
    except ValueError:
        vyska = input("cislo.. ")





if vyska<87:
    povoleni=False
    print("Jste moc nízký..")

if povoleni:
    vek= input("Zadejte věk: ")
    while type(vek) != int:
        try:
            vek=int(vek)
        except ValueError:
            vek= input("cislo.. ")
            
            


    if vek<12:
        cena = 50
    if vek>=12 and vek<18:
        cena=100
    if vek>=18 and vek<65:
        cena=150

    fotka = input("Chcete fotku? (ano/ne): ")
    if fotka=="ano":
        cena+=40
    
    print(f"Vstupné je {cena}kč.")

    """
# suma=0
# for i in range (1, 11):
#     print(i, end=" ")
#     suma += i
# print("")
# print(suma)

# slovo = "python"
# for i in range (len(slovo)):
#     print(slovo[i])
# for i in slovo:
#     print(i)


import random
run = True
pokus = 0
# for i in range (5):
#     nahoda = random.randint(1,10)
#     print(nahoda)
rozmezi = int(input("zadejte rozmezi 0 - ?: "))

while(run):
    pokus = pokus+1
    guess = int(input("zadejte odhad: "))
    ra = random.randint(0,rozmezi)
    print("random cislo --> ", ra)
    if guess == ra:
        run= False
print("wow. jenom ", pokus, " pokusu")