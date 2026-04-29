import math

def jedna():
    a = int(input("zadejte cele cislo: "))

    obsah = a*a
    obvod = a*4
    if(a>0):
        print("kladne")


    if(((a%2)==0) and a!=0):
        print("sude")
    elif(a!=0):
        print("liche")

    print(f"obsah je >> {obsah} metrů^2")
    print(f"obvod je >> {obvod} metrů")
        
    if(a<0):
        print("zaporne")
        abs(obsah)
        abs(obvod)
    
        print(f"{obsah} metrů^2 = {obsah * 1000} milimetrů^2")
        print(f"{obvod} metrů = {obvod * 1000} milimetrů")

    # if(a!=0):
    #     obsah = a*a
    #     obvod = a*4
    #     print(f"obsah je >> {obsah} metrů^2 = {obsah * 1000} milimetrů^2")
    #     print(f"obvod je >> {obvod} metrů = {obvod * 1000} milimetrů")
    if(a==0):
        print("Zadána nula, s ní nepočítám")

def dva():

    a = float(input("zadejte poloměr v metrech: "))
    
    objem = (4/3) * math.pi * (a*a*a)
    litry = objem*1000
    print(litry)
    print(f"clovek by vydrzel {litry/5} dni")

def tri():
    # kralik = int(input("pocet kraliku: "))
    # slepice = int(input("pocet slepic: "))

    # hlava=0
    # nohy=0
    # hlava += (kralik+slepice)
    # nohy += (slepice*2 + kralik*4)

    # print(f"nohy: {nohy}")
    # print(f"hlavy: {hlava}")


    inputhlavy = int(input("pocet hlav: "))
    inputnohy = int(input("pocet nohou: "))

    knohy = inputnohy//4
    kralici = knohy
    slepice = inputhlavy - kralici
    # snohy = inputnohy - knohy
    # shlavy = snohy//2
    # khlavy=inputhlavy-shlavy



    # print(f"knohy{knohy} , snohy{snohy}, shlavy{shlavy}, khlavy{khlavy}")
    print(f"kralici{kralici}, slepice{slepice}")
tri()
