import time


def isPrime(x):
    for fraction in range(2, x):
        if x % fraction == 0:
            return False
    return True      


def factorization(modulo):
    for factor in range(3, modulo, 2):
        if modulo % factor == 0:
            return factor, int(modulo/factor)
    raise Exception("The modulo {} isn't created by two factors!!!".format(modulo))


def inversion(public_key, PHI):
    private_key = 1
    if isPrime(PHI):
        return eulerInversion(public_key, PHI)
    else:
        while True:
            if (public_key * private_key) % PHI == 1:
                return private_key
            else:
                private_key += 1


def eulerInversion(public_key, PHI):
    private_key = (public_key ** (PHI - 2)) % PHI
    return private_key


def extendedEuclidianAlgirithmInversion(PHI, public_key):
    if PHI == 0:
        return 0, 1
    else:
        x, y = extendedEuclidianAlgirithmInversion(public_key % PHI, PHI)
        return y - (public_key//PHI) * x, x


def signCheck(private_key, public_key, PHI):
    if (private_key*public_key) % PHI == 1:
        if private_key < 0:
            return private_key % PHI
        return private_key
    else:
        private_key *= (-1)
        if private_key < 0:
            return private_key % PHI
        return private_key
