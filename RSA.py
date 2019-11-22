import time
from yaspin import yaspin
from prettytable import PrettyTable
from functions import *

# Only main thread can access this code 
if __name__ == "__main__":
    print("""
      ____  ____    _    
     |  _ \/ ___|  / \   
     | |_) \___ \ / _ \  
     |  _ < ___) / ___ \ 
    .|_| \_\____/_/   \_\.
    --public key cracking--                    
                        """)

    # Inserting parameters
    while True:
        print("---enter parametrs---")
        public_key = input("Enter public key: ")
        modulo = input("Enter modulo: ")
        input("-press enter to begin-")
        print("\n")

        # Catching invalid input
        if numCheck(modulo, public_key) == True:
            public_key = int(public_key)
            modulo = int(modulo)
            break
        print("\033[;33mError: All input parameters must be numbers!\033[0;0m\n")
    
    # Finding p, q
    with yaspin(text="Finding primes...", color="yellow") as spinner:
        factors, factorization_time = factorization_switch(modulo)
        spinner.ok("✔ \033[0;32m[Done]\033[0;0m")
        print("\033[1;30m  [" + str(factorization_time) + "]  Time for execution\033[0;0m")

    # Back check before continuing
    with yaspin(text="Checking values...", color="yellow") as spinner:
        start_time = time.time()
        if isPrime(factors[0]) == False or isPrime(factors[1]) == False:
            print("\n\nFatal Error: Modulo is not created by two prime factors!\n")
            os._exit(0)
        if factors[0] * factors[1] != modulo:
            print("\n\nFatal Error: Failed to find factors!\n")
            os._exit(0)
        end_time = time.time()
        final_time = end_time - start_time
        spinner.ok("✔ \033[0;32m[Done]\033[0;0m")
        print("\033[1;30m  [" + str(final_time) + "]  Time for execution\033[0;0m")

    # Computing PHI
    PHI = (factors[0]-1) * (factors[1]-1)
        
    # Generating private key
    with yaspin(text="Generating private key...", color="yellow") as spinner:
        start_time = time.time()
        not_inversion, private_key = extendedEuclidianAlgirithmInversion(PHI, public_key)
        end_time = time.time()
        final_time = end_time - start_time
        spinner.ok("✔ \033[0;32m[Done]\033[0;0m")
        print("\033[1;30m  [" + str(final_time) + "]  Time for execution\033[0;0m")

    # Converting negative private key to positive value
    private_key = signCheck(private_key, public_key, PHI)  

    # Back check before continuing
    with yaspin(text="Checking private key...", color="yellow") as spinner:
        start_time = time.time()
        if (private_key * public_key) % PHI != 1:
            print("\n\nFatal Error: Failed to generate valid private key!\n")
            os._exit(0)
        end_time = time.time()
        final_time = end_time - start_time
        spinner.ok("✔ \033[0;32m[Done]\033[0;0m")
        print("\033[1;30m  [" + str(final_time) + "]  Time for execution\033[0;0m")

    # Outputing all vulues for user 
    print("\n")
    output = PrettyTable()
    output.field_names = ["OUTPUT TABLE", " "]
    output.add_row(["Factors of modulo (primes)",str(factors[0]) + ", " + str(factors[1])])
    output.add_row(["Euler's phi",PHI])
    output.add_row(["\033[;33mPrivate key\033[0;0m","\033[;33m" + str(private_key) + "\033[0;0m"])
    print (output)
    print("\033[0;0m\n")

    # Exit
    input("Press enter to exit...")
