import time, multiprocessing, os

BLUE   = '\33[92m'
YELLOW = '\033[;33m'
GREEN  = '\033[0;32m'
GRAY   = '\033[1;30m'
RED    = '\033[91m'
END    = '\033[0;0m'

# Function for testing prime value
def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

# Generator of prime nubers candidates list _OLD_
def gen_primes(start, end):
    primes = set()
    for n in range(start, end):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

# Switch for optimal factorization method based on modulo size
def factorization_switch(modulo):
    bit_size = len(str(bin(modulo).replace("0b", ""))) #size of modulo in bit
    if bit_size < 10:
        factors, factorization_time = factorization_basic(modulo)
    else:
        factors, factorization_time = factorization_multi(modulo, bit_size)
    return factors, factorization_time

# Function for factorization with single process
def factorization_basic(modulo):
    start_time = time.time()
    factors = []
    for factor in range(3, modulo, 2):
        if modulo % factor == 0:
            factors.append(factor)
            factors.append(int(modulo/factor))
            end_time = time.time()
            return factors, end_time - start_time
    print(RED + "\n\nFatal Error: Modulo is not created by two prime factors!\n" + END)
    os._exit(0)

# Function compatible with multiprocess factorization
def factorization_core(modulo, start, end, results, processIsNotRunning):
        for factor in range(start, end, 2):
            if modulo % factor == 0:
                results[0] = factor
                results[1] = int(modulo / factor)
                return 1
        if processIsNotRunning[0] == 1:
            processIsNotRunning[1] = 1
        else:
            processIsNotRunning[0] = 1
        return 0

# Function for preparing multiprocess factorization
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

    # Assigning
    start_p1 = 3
    end_p1 = int(start)
    start_p2 = int(start)
    end_p2 = (int(end) + 1) # +1 because of range()
     

    if __name__ == "functions":
        results = multiprocessing.Array('i', 2) # Make shared memory
        processIsNotRunning = multiprocessing.Array('i', 2) # Shared status of each process 

        # Loop for initiating both processes with diferent parameters
        for count in range(1, 3):
            if count == 1:
                process = multiprocessing.Process(target=factorization_core, args=[modulo, start_p1, end_p1, results, processIsNotRunning])
                
            if count == 2:
                process = multiprocessing.Process(target=factorization_core, args=[modulo, start_p2, end_p2, results, processIsNotRunning])  
        
        # Starting both processes 
        process.start()
        
        # Catching main thread and waiting for both results
        while True:
            if results[1] != 0:  
                break
            if processIsNotRunning[0] == 1 and processIsNotRunning[1] == 1:
                print(RED + "\n\nFatal Error: Modulo is not created by two prime factors!**\n" + END)
                os._exit(0)

        # Terminating any left processes 
        if process.is_alive():
            process.terminate()
        
        # Returning results
        end_time = time.time()
        return results, end_time - start_time

# Function for finding inversion in modulo _OLD_
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

# Function of Euler inversion _OLD_
def eulerInversion(public_key, PHI):
    private_key = (public_key ** (PHI - 2))%PHI
    return private_key

# Function for finding private key with Extended Euclidian Algorithm
def extendedEuclidianAlgirithmInversion(PHI, public_key):
	if PHI == 0:
		return (0, 1)
	else:
		x, y = extendedEuclidianAlgirithmInversion(public_key % PHI, PHI)
		return (y - (public_key//PHI) * x, x)

# Function checking if private key is negative value and converting it to positive value
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

# Function checking if convertion to int is possible
def numCheck(modulo, public_key):

    if len(modulo) == 0 or len(public_key) == 0:
        return False

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in modulo:
        if numbers.count(i) == 0:
            return False

    for i in public_key:
        if numbers.count(i) == 0:
            return False
    
    return True
