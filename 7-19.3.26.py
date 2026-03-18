def jedna():
    vstup = input("zadejte palindrom: ")
    slovo=vstup.replace(" ", "")
    delka = len(slovo)
    check=False
    sudy= delka
    if((delka % 2)==0):
        pul = int(delka/2)
        sub1= slovo[0:pul]
        sub2=slovo[delka:pul-1:-1]
        if(sub2==sub1):
            check=True  

    else:
        pul=int(delka/2)
        sub1=slovo[:pul]
        sub2=slovo[delka:pul:-1]
        if(sub2==sub1):
            check=True


    print(sub1,sub2)
    if(check):
        print("je to palindrom: ",slovo)

def dva():
    vstup = int(input("zadejte faktorial: "))
    while(vstup<0):
        vstup = int(input("zadejte kladne cislo..  "))
    if(vstup == (1 or 0)):
        vysledek=1

    else:

        vysledek=1
        for i in range (1,vstup+1):
            vysledek*=i
            print(i, end="")
            if(i!=vstup):
                print(" * ", end="")
            else:
                print("\n")
    
    print(f"{vstup}! = {vysledek}")



dva()