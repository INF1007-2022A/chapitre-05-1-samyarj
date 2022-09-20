#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

# Écrire un programme qui lit un nombre et affiche sa valeur absolue, sans utiliser de fonction avancée
def convert_to_absolute(number: float) -> float:
    if number < 0:
        return (number/(-1))
    return number # pas besoin de else statement
    # return abs(number);

# Dans un conte américain, huit petits canetons s'appellent respectivement : Jack, Kack, Lack, Mack, Nack, Oack, Pack et Qack.
# Écrire un petit script qui génère tous ces noms à partir des deux chaînes suivantes : prefixes = 'JKLMNOPQ' et suffixe = 'ack'

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = list() # store results in a list
    for letter in prefixes:
        generated_name = f'{letter}{suffixe}'
        names.append(generated_name)
    return names

#Calculer la somme des 100 premiers nombres entiers premiers excluant le nombre 1
def prime_integer_summation() -> int:
    p = list() # not prime
    prime_numbers = []
    # trouver les nombres primes
    for i in range(2, 101): # domain = [2, 100]
        for k in range(2, i):
            if i % k == 0:
                p.append(i)
        if i not in p:
            prime_numbers.append(i)

    # faire la somme
    result = int() #
    for j in prime_numbers:
        result += j
    return result


def factorial(number: int) -> int:
    # n! = n(n-1)! ; 0! = 1
    if number > 1 : # to avoid a stiaution where the result is 0
        result = number * (number-1)
        n = (number-2)
        if n == 0: # 2! = 2
            return result
        else: # for every other case
            while n > 1:
                result *= n
                n -= 1
            return result
    else:
        return number

def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue # or pass
        else:
            print(i)

# continue documentation : https://docs.python.org/3.10/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
def verify_ages(groups: List[List[int]]) -> List[bool]:
    accept = list()
    # analyse criteria group by group
    for group in groups: # each group is an iteration
        # size criteria; separate from age criteria
        if (len(group) <= 3) or (len(group) > 10):
            accept.append(False)
            continue
        # age criteria
        if 25 in group:
            accept.append(True)
            continue # go to next iteration as soon as you see 25
        if min(group) < 18:
            accept.append(False)
            continue
        if (50 in group) and (max(group) > 70):
            accept.append(False)
            continue
        accept.append(True)
    return accept


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
