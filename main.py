print ("KALKULACKA:")
x=int(input("zadej cislo"))
y=int(input("zadej druhy cislo"))
z=input("zadej znak operace")
vysledek = 0

if (z=="+"):
    vysledek = x+y
    print("vysledek = " , vysledek , "ok?")

if (z=="-"):
    vysledek = x-y
    print("vysledek = " , vysledek , "ok?")