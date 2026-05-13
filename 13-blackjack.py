import random
cards = [2,3,4,5,6,7,8,9,10,"A","J","Q"]
balance = 500
bet=0
max = 21
konec = False
playerCards = []
dealerCards = []
vyber=""
vysledek = ""
playerCisla=[]
dealerCisla = []


def randomkarta():
    randomkarta = random.choice(cards)
    return randomkarta

def naInt(karta):
    if (karta=="Q" or karta=="J" or karta=="K"):
        karta=10
    if(karta=="A"):
        karta=11
    return karta

def hra(balance, vyber, bet):
    while(konec==False):
        print("balance >> "+str(balance))
        bet = int(input("zadejte sazku: "))
        print("sazka je >> "+str(bet))
        if(bet > balance):
            bet = balance
            balance = 0
        else:
            balance-=bet
        
        playerCards.append(randomkarta())
        # playerCards.append("A")
        
        dealerCards.append(randomkarta())
        # print("prvni karta - "+ str(playerCards))
        playerCisla.append(naInt(playerCards[0]))
        dealerCisla.append(naInt(dealerCards[0]))

        playerCards.append(randomkarta())
        dealerCards.append(randomkarta())
        playerCisla.append(naInt(playerCards[1]))
        dealerCisla.append(naInt(dealerCards[1]))
        print("prvni dve karty - "+ str(playerCards) + "\n soucet hrace => "+str(sum(playerCisla)))
        print("druha karta dealera - "+ str(dealerCards[1]) + "\n soucet dealera => "+str((dealerCisla[1])))

        

        vyber = input("hit/stay: ")
        if(vyber == "hit"):
            playerCards.append(randomkarta())
            playerCisla.append(naInt(playerCards[2]))
            print("hrac - "+str(playerCards) + "\n soucet hrace => "+str(sum(playerCisla)))
            
        if(sum(playerCisla)>21):
            konec==True
            return "prohra"

        # print("....")
        print("dealer - "+str(dealerCisla) + "\n soucet dealera => "+str(sum(dealerCisla)))
        if(sum(dealerCisla)<17):
            dealerCards.append(randomkarta())
            dealerCisla.append(naInt(dealerCards[2]))
            print("dealer si bere dalsi kartu.. ")
            print("dealer - "+str(dealerCisla) + "\n soucet dealera => "+str(sum(dealerCisla)))

        if(sum(playerCisla)>sum(dealerCisla)):
            konec == True
            return "vyhra"
        elif(sum(playerCisla) == sum(dealerCisla)):
            return "remiza"
        else:
            return "prohra"


vysledek = hra(balance, vyber, bet)
print(vysledek)