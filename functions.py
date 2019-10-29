def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

def factorization(x):
    factors = []
    for factor in range(3,x,2):
        print(factor)
        if x%factor == 0:
            factors.append(factor)
            if len(factors) == 2:
                if factors[0] * factors[1] == x:
                    return factors
    return 0

def inversion(public_key, PHI):
    private_key = 1
    if isPrime(PHI) == True:
        return eulerInversion(public_key, PHI)
    else:
        while True:
            if (public_key * private_key)%PHI == 1:
                return private_key
            else:
                print(private_key)
                private_key += 1

def eulerInversion(public_key, PHI):
    private_key = (public_key ** (PHI - 2))%PHI
    return private_key
