import time

def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

def factorization(x):
    start_time = time.time()
    factors = []
    for factor in range(3,x,2):
        if x%factor == 0:
            factors.append(factor)
            factors.append(int(x/factors[0]))
            if len(factors) == 2:
                if factors[0] * factors[1] == x:
                    end_time = time.time()
                    return factors, end_time - start_time
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
                private_key += 1

def eulerInversion(public_key, PHI):
    private_key = (public_key ** (PHI - 2))%PHI
    return private_key

def extendedEuclidianAlgirithmInversion(PHI, public_key):
	if PHI == 0:
		return (0, 1)
	else:
		x, y = extendedEuclidianAlgirithmInversion(public_key % PHI, PHI)
		return (y - (public_key//PHI) * x, x)

def signCheck(private_key, public_key, PHI):
    if (private_key*public_key)%PHI == 1:
        if private_key < 0:
            return private_key%PHI
        return private_key
    else:
        private_key *= (-1)
        if private_key < 0:
            return private_key%PHI
        return (private_key)