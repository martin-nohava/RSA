import time
import threading

def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

def threaded_factorization(x):
# rozložení čísla do dvou vláken
    if len(str(x)) > 10:
        first_part = str(x)[len(str(x))-10:] #posledních 10 cislic cisla x
        rest_of_x = str(x)[:len(str(x))-10] + ("0" * 10) #zbytek cisla
        
        try:
            thread.start_new_thread(factorization(int(first_part)))
            thread.start_new_thread(factorization(int(rest_of_x)))
        except:
            print ("Error: unable to start threaded factorization!")


def factorization(x):
    start_time = time.time()
    factors = []
    for factor in range(3,x,2):
        if x%factor == 0:
            factors.append(factor)
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
        return private_key
    else:
        return (private_key*(-1))

""" def split(string): 
    return [char for char in string] """