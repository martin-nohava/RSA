import time
import threading

def isPrime(x):
    for fraction in range(2,x):
        if x%fraction == 0:
            return False
    return True      

class default_thread (threading.Thread):
    def __init__(self, threadID, name, modulo):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.modulo = modulo
    def run(self):
        print ("Starting " + self.name)
        factorization(self.modulo)
        print ("Exiting " + self.name)

def threaded_factorization(x):
# rozložení čísla do dvou vláken
    if len(str(x)) > 10:
        first_part = str(x)[len(str(x))-10:] #posledních 10 cislic cisla x
        rest_of_x = str(x)[:len(str(x))-10] + ("0" * 10) #zbytek cisla
                
        try:
            """ factors1, factorization_time1 = my_thread1 = thread.start_new_thread(factorization, (int(first_part)))
            factors2, factorization_time2 = thread.start_new_thread(factorization, (int(rest_of_x)))
 """
            thread1 = default_thread(1, "Thread-1", int(first_part))
            thread2 = default_thread(2, "Thread-2", int(rest_of_x))
            thread1.run()
            thread2.run()

            if len(factors1) == 2:
                return factors1, factorization_time1
            else:
                return factors2, factorization_time2
        except:
            print ("Error: unable to start threaded factorization!")
            input()

    else:
        factorization(x)

def factorization(x):
    start_time = time.time()
    factors = []
    for factor in range(3,x,2):
        if x%factor == 0:
            factors.append(factor)
            factors.append(x/factor)
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