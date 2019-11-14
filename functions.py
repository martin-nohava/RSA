import time

def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

def primeNumbersPseudogenerator(modulo):
    start_time = time.time()
    bit_size = len(str(bin(modulo).replace("0b", ""))) #velikost v bit
    if bit_size%2 != 0:
        bit_size += 1
    start = 2 ** ((bit_size/2)-1)
    end = 2 ** (bit_size/2)
    if start%2 == 0:
        start -= 1
    start = int(start)
    end = int(end)

    candidates = [n for n in range(start, end, 2)]


    for i in range(len(candidates)):
        candidates = [n for n in candidates if n == candidates[i] or n % candidates[i] > 0]
        if i > 100:
            break
    end_time = time.time()
    return candidates, end_time - start_time

def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

def factorization(x, candidates):
    start_time = time.time()
    factors = []
    for factor in candidates:
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