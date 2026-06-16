import random


end=False
print("1 pro 1-10\n2 pro 1-50\n3 pro 1-100\n4 pro vlastni rozsah\n5 pro konec")
rozsah = int(input("zadejte vyber: "))

if(rozsah==1):
    x=10
if(rozsah==2):
    x=50
if(rozsah==3):
    x=100
if(rozsah==4):
    x=int(input("zadejte vlastni rozsah: "))
if(rozsah==5):
    x=1
    end=True


rCislo=random.randrange(0,x)
min=0
max=x

try:

    while(end==False):

        check=input(f"je tve cislo vetsi nez {rCislo}? \n(a/n): ")
        
        
        if(check=="a"):
            min=rCislo
            
        else:
            max=rCislo
            
        rCislo=random.randrange(min+1,max)
        if(max-1==min):
            end=True
            guess = rCislo+1
            print(f"\nvase cislo je {guess}")
    
except:
    end=True
    if(check=="a"):

        guess = rCislo+1
    else:
        guess=rCislo
    print(f"\nvase cislo je {guess}")
