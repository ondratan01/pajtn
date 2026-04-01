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

        if vstup != 0:
            if min>vstup:
                min=vstup
            if max<vstup:
                max=vstup
        
       
    inputseznam.pop(len(inputseznam)-1)
    print("max je ",max,"min je ",min)
    rozdil = max-min
    minstring = ""
    maxstring = ""

    if(min <0):
        minstring = (f"({min})")
    else:
        minstring = min

    if(max <0):
        maxstring = (f"({max})")
    else:
        maxstring = max


    print(f"rouzdil {maxstring} - {minstring} je {rozdil}")

def ctyri():
    vstup = 1
    nasobek = 0
    inputseznam = []
    endseznam = []
    

    while vstup!=0:
        
        vstup = int(input("zadejte cislo do listu: "))
        inputseznam.append(vstup)

    inputseznam.pop(len(inputseznam)-1)
    nasobek = int(input("zadejte nasobek: "))

    # for i in inputseznam:
    #     if ((inputseznam[i] % nasobek) != 0):
    #         endseznam.append(inputseznam[i])

    for i in range(0, len(inputseznam)):
        if ((inputseznam[i] % nasobek) != 0):
            endseznam.append(inputseznam[i])

    print(endseznam)
ctyri()


