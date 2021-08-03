import sys

from random import randrange
print("Ahoj, vitej ve hre oko bere.")
hodnota = 0
while hodnota < 21:
    print("Tvuj soucet bodu je:",hodnota)
    odpoved = input("Chces otocit kartu?")
    if odpoved == "ano":
        karta = randrange(2, 11)
        print("Tvoje hodnota je:", karta)
        hodnota = hodnota + karta
    elif odpoved == "ne":
        break
    else:
        print("Zadej pouze ano/ne. Dekujeme.")
if hodnota == 21:
    print("Gratulujeme, vyhral jsi.")
elif hodnota > 21:
    print("Bohuzel jsi prohral. Zkus stesti od zacatku.")
else:
    print("Skoda chybelo ti",21 - hodnota, "bodu.")

