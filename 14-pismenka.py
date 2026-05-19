import os
import time
# os.system('cls' if os.name == 'nt' else 'clear')


os.system('cls')
slovo = input("zadejte slovo: ")
remaining = slovo
for i in range(len(slovo)): 
    os.system('cls') 
    pismenko = slovo[i]
    print(slovo[i:])
    for x in range(10):
        print(pismenko)
        time.sleep(0.1)