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

import requests
from threading import Thread


def send_calculation(operation, first_number, second_number, identifier):
    data = requests.post(
        f"https://calc.wmwmw.cz/api/{operation}/",
        json={"first": first_number, "second": second_number},
    ).json()
    print(f"\n#{identifier} Výsledek operace {operation} je {data['result']}")


def get_number(identifier):
    while True:
        number = input(f"Zadej {identifier} číslo: ")
        if number.isdigit():
            return int(number)


def main():
    i = 0
    threads = []
    while True:
        selected_operation = input("Zadej operaci (add, sub, mul) nebo end: ")

        if selected_operation == "end":
            break
        elif selected_operation in ["add", "sub", "mul"]:
            first_number = get_number("první")
            second_number = get_number("druhé")
            thread = Thread(
                target=send_calculation,
                args=(selected_operation, first_number, second_number, i),
            )
            thread.start()
            print(
                f"Operace {selected_operation} byla odeslána"
                f"na server, výsledek bude zobrazen pod identifikátorem {i}"
            )
            threads.append(thread)
            i += 1
        else:
            print("Nesprávná operace")

    for thread in threads:
        thread.join()

    print("Výsledky byly zobrazeny, program končí.")


if __name__ == "__main__":
    main()

data = input("Napiš data: ")
data_type = input("Napiš typ: ")


TYPES = {
    "str": str,
    "int": lambda x: int(x),
    "float": float,
    "bool": bool,
}


if func := TYPES.get(data_type):
    data = func(data)


print(f"{type(data)}: {data}")