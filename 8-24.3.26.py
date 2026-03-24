def kalkulacka():
    prvni = int(input("zadejte 1. cislo: "))
    druhy = int(input("zadejte 2. cislo: "))
    znak = input("zadejte znak pro vypocet: ")
    vysledek=0
    if znak=='+':
        vysledek = plus(prvni,druhy)
    if znak=='-':
        vysledek=minus(prvni,druhy)
    if znak=='*':
        vysledek=krat(prvni,druhy)
    if znak=='/':
        vysledek=deleno(prvni,druhy)

    # match(znak):
    #     case '+': 


    print(vysledek)
def plus(a,b):
    a+=b
    return a
def minus(a,b):
    a-=b
    return a
def krat(a,b):
    a*=b
    return a
def deleno(a,b):
    a/=b
    return a




def KNP():
    import random
    
    moznosti = ['kamen', 'nuzky', 'papir']
    clovekbody=0
    pocitacbody=0
    # pocitac = random.randrange(0,3)
    # print(pocitac)
    

    while((clovekbody!=3) and (pocitacbody!=3)):
        vstup = input("kamen/nuzky/papir?: ")
        pocitac = random.choice(moznosti    )
        print("   \t     AI >> ",pocitac)

        if pocitac=='nuzky':
            if vstup == 'papir':
                pocitacbody+=1
            elif vstup == 'kamen':
                clovekbody+=1
            # else continue
        if pocitac == 'kamen':
            if vstup == 'papir':
                clovekbody+=1
            elif vstup == 'nuzky':
                pocitacbody+=1
            # else continue
        if pocitac == 'papir':
            if vstup == 'kamen':
                pocitacbody+=1
            if vstup == 'nuzky':
                clovekbody+=1
        
        print(f"Ty = {clovekbody}b")
        print(f"AI = {pocitacbody}b")
        print("\n")
        if(clovekbody==3):
            print("\tDobrá práce!")
        if(pocitacbody==3):
            print("\tSmůla no..")

KNP()