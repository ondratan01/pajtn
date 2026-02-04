print ("KALKULACKA:")
x=int(input("zadej cislo: "))
y=int(input("zadej druhy cislo: "))
z=input("zadej znak operace( + | - | * | / | % | // ): ")
vysledek = 0
check = 1

if (z=="+"):
    vysledek = x+y
    
elif (z=="-"):
    vysledek = x-y

elif (z=="*"):
    vysledek = x*y

elif (z=="/"):
    vysledek = x/y

elif (z=="//"):
    vysledek = x//y
    
elif (z=="%"):
    vysledek = x%y

else:
    print ("wtf")
    check = 0

if check !=0:
    print("vysledek = " , vysledek , "ok?")