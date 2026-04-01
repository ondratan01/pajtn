def jedna():
    seznam = list(range(1,6))
    inputseznam = []
    print(seznam)

    for _ in range(5):
        
        vstup = int(input("zadejte cislo do listu: "))
        inputseznam.append(vstup)
        
       
    # inputseznam.pop(len(inputseznam)-1)
    print(inputseznam)










def dva():
    vstup = 1
    inputseznam = []
    

    while vstup!=0:
        
        vstup = int(input("zadejte cislo do listu: "))
        inputseznam.append(vstup)
        
       
    inputseznam.pop(len(inputseznam)-1)
    print(inputseznam)
    print(len(inputseznam))


def tri():
    vstup = 1
    pocet = 0
    inputseznam = []
    

    while vstup!=0:
        
        vstup = int(input("zadejte cislo do listu: "))
        inputseznam.append(vstup)
        

        if (vstup != 0) and (pocet != 1):
            min = vstup
            max = vstup
            pocet+=1

        if min<vstup:
            min=vstup
        if max>vstup:
            max=vstup
        
       
    inputseznam.pop(len(inputseznam)-1)
    print(inputseznam)
tri()





