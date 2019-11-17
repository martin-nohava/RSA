import time

def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

def gen_primes(start, end):
    primes = set()
    for n in range(start, end):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

def factorization(modulo):
    start_time = time.time()
    factors = []
    # first trying to search for correct prime in midlle bit of modulo (asuming that primes of modulo are approximately similar in size)
    bit_size = len(str(bin(modulo).replace("0b", ""))) #size of modulo in bit
    if bit_size%2 != 0:
        bit_size += 1
    start = 2 ** ((bit_size/2)-1)
    end = 2 ** (bit_size/2)
    if start%2 == 0:
        start -= 1
    start = int(start)
    end = int(end)
    #RANGE END

    if start%2 == 0:
        start -= 1

    for factor in range(start, end,2):
        if modulo%factor == 0:
            factors.append(factor)
            factors.append(int(modulo/factors[0]))
            if len(factors) == 2:
                if factors[0] * factors[1] == modulo:
                    end_time = time.time()
                    return factors, end_time - start_time
                    
    # if first for failed to find solution we use bruteforce, but only on untested parts of range        
    # part no. 1      
    for factor in range(3,(start+1),2):
        if modulo%factor == 0:
            factors.append(factor)
            factors.append(int(modulo/factors[0]))
            if len(factors) == 2:
                if factors[0] * factors[1] == modulo:
                    end_time = time.time()
                    return factors, end_time - start_time    
    # lichost
    if end%2 == 0:
        end -= 1
    # Part no. 2
    for factor in range(end,modulo,2):
        if modulo%factor == 0:
            factors.append(factor)
            factors.append(int(modulo/factors[0]))
            if len(factors) == 2:
                if factors[0] * factors[1] == modulo:
                    end_time = time.time()
                    return factors, end_time - start_time

    return print("Error: factoization of modulo failed!")

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