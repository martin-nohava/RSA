import time
import multiprocessing

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

def factorization_switch(modulo):
    bit_size = len(str(bin(modulo).replace("0b", ""))) #size of modulo in bit
    if bit_size < 10:
        factors, factorization_time = factorization_basic(modulo)
    else:
        factors, factorization_time = factorization_multi(modulo, bit_size)
    return factors, factorization_time

def factorization_basic(modulo):
    start_time = time.time()
    factors = []
    for factor in range(3, modulo, 2):
        if modulo % factor == 0:
            factors[0] = factor
            factors[1] = int(modulo/factor)
            end_time = time.time()
            return factors, end_time - start_time
    raise Exception("The modulo {} isn't created by two factors!".format(modulo))
# Function for multiprocess factorization
def factorization_core(modulo, start, end, results):
        for factor in range(start, end, 2):
            if modulo % factor == 0:
                #print("factor WAS found in range of [{},{}]".format(start, end))
                results[0] = factor
                results[1] = int(modulo / factor)
                return 1

        #print("factor was NOT found in range of [{},{}]".format(start, end))
        return 0

def factorization_multi(modulo, mod_size):
    start_time = time.time()
    
    # Finding start, end from modulo
    if mod_size%2 != 0:
        start = 2 ** (int(mod_size/2))
        end = 2 ** ((int(mod_size/2)) + 1)
    else:
        start = 2 ** ((mod_size/2) - 1)
        end = 2 ** (mod_size/2)
    # Making sure start, end are odd numbers
    if start%2 == 0:
        start -= 1

    if end%2 == 0:
        end -= 1
    # Assigning
    start_p1 = 3
    end_p1 = int(start)
    start_p2 = int(start)
    end_p2 = (int(end) + 2) # +1 because of range() and another +1 because if end%2 == 0:
     

    if __name__ == "functions":
        results = multiprocessing.Array('i', 2)          # Make shared memory

        for count in range(1, 3):
            if count == 1:
                process = multiprocessing.Process(target=factorization_core, args=[modulo, start_p1, end_p1, results])
                
            if count == 2:
                process = multiprocessing.Process(target=factorization_core, args=[modulo, start_p2, end_p2, results])  
        
        process.start()
        # Catching main thread and waiting for both results
        while True:
            if results[1] != 0:
                break
        # Terminating any left processes 
        if process.is_alive():
            process.terminate()
        # Returning results
        end_time = time.time()
        return results, end_time - start_time


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