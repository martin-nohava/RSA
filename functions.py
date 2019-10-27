def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

def factorization(x):
    factors = []
    for factor in range(2,x):
        if x%factor == 0:
            factors.append(factor)
            if len(factors) == 2:
                if factors[0] * factors[1] == x:
                    return factors
    return 0

def algorithmSwitch(public_key, PHI):
    x = public_key
    y = PHI
    while y != 0:
        (x, y) = (y, x % y)
    if x == 1:
        return extendedEuclidanAlgorithm(public_key, PHI)
    else:
        return inversion(public_key, PHI)

def inversion(public_key, PHI):
    private_key = 1
    if isPrime(PHI) == True:
        return eulerInversion(public_key, PHI)
    else:
        while True:
            if (public_key * private_key)%PHI == 1:
                return private_key
            else:
                private_key += 1

def eulerInversion(public_key, PHI):
    private_key = (public_key ** (PHI - 2))%PHI
    return private_key

def extendedEuclidanAlgorithm(public_key, PHI):
	if public_key == 0:
		return (PHI, 0, 1)
	else:
		x, y = extendedEuclidanAlgorithm(PHI % public_key, public_key)
		return (y - (PHI//public_key) * x)
