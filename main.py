"""ce programme permet de vérifier si un nombre entier est premier ou pas"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """ Fonction vérifiant si un entier p est premier"""
    if p==1:
        return False
    for i in range(2, int(sqrt(p))+1):
        if p%i==0:
            return False
    return True

#### Fonction principale


def main():
    """ Fonction principale affichant les nombres entiers de 0 à 99"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
