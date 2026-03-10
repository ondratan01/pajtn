import math
def jedna():
    jedna=float(input("zadejte 1. cislo: "))
    dve=float(input("zadejte 2. cislo: "))
    operator=input("zadejte operator: ")

    match operator:
        case '+':
            print("vysledek >> ", jedna+dve)
        case '-':
            print("vysledek >> ", jedna-dve)
        case '*':
            print("vysledek >> ", jedna*dve)
        case '/':
            print("vysledek >> ", jedna/dve)
        case '//':
            print("vysledek >> ", jedna//dve)
        case '%':
            print("vysledek >> ", jedna%dve)
        case 'mocnina':
            print("vysledek >> ", math.pow(jedna, dve))
        case 'odmocnina':
            print("druha odmocnina prvniho cisla >> ", math.sqrt(jedna))
        case _:
            print("meli jste zadat operator..")

def dve():
    # cisla = [1,2,3,4,5,6,7,8,9,0]
    vstup = input("zadejte heslo: ")
    pouzitelne = True
    if len(vstup)<8:
        pouzitelne=False
    elif (vstup.islower() and vstup.isalpha()) and (vstup.isupper() and vstup.isalpha()):
        print("hodne slabe")
    elif vstup.isnumeric and (("!" in vstup) or ("?" in vstup)):
        print("hodne silne")
    elif (vstup.islower() and vstup.isalpha()) and (vstup.isupper() and vstup.isalpha()) or vstup.isnumeric:
        print("silnejsi")
    else:
        print("slabe celkem")


dve()