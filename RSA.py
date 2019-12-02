import time
from yaspin import yaspin
from prettytable import PrettyTable
import functions as function

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
        print("  ---enter parametrs---")
        public_key = input("  Enter public key: ")
        modulo = input("  Enter modulo: ")
        input("  -press enter to begin-")
        print("\n")

        # Catching invalid input
        if function.numCheck(modulo, public_key) == True:
            public_key = int(public_key)
            modulo = int(modulo)
            break
        print (function.YELLOW + "\nError: All input parameters must be numbers!\n" + function.END)
    
    # Finding p, q
    with yaspin(text="Finding primes...", color="yellow") as spinner:
        factors, factorization_time = function.factorization_switch(modulo)
        spinner.ok("✔ " + function.GREEN + "[Done]" + function.END)
        print(function.GRAY + "  [" + str(factorization_time) + "]  Time for execution" + function.END)

    # Back check before continuing
    with yaspin(text="Checking values...", color="yellow") as spinner:
        start_time = time.time()
        if function.isPrime(factors[0]) == False or function.isPrime(factors[1]) == False:
            print(function.RED + "\n\nFatal Error: Modulo is not created by two prime factors!\n" + function.END)
            function.os._exit(0)
        if factors[0] * factors[1] != modulo:
            print(function.RED + "\n\nFatal Error: Failed to find factors!\n" + function.END)
            function.os._exit(0)
        end_time = time.time()
        final_time = end_time - start_time
        spinner.ok("✔ " + function.GREEN + "[Done]" + function.END)
        print(function.GRAY + "  [" + str(final_time) + "]  Time for execution" + function.END)

    # Computing PHI
    PHI = (factors[0]-1) * (factors[1]-1)
        
    # Generating private key
    with yaspin(text="Generating private key...", color="yellow") as spinner:
        start_time = time.time()
        not_inversion, private_key = function.extendedEuclidianAlgirithmInversion(PHI, public_key)
        end_time = time.time()
        final_time = end_time - start_time
        spinner.ok("✔ " + function.GREEN + "[Done]" + function.END)
        print(function.GRAY + "  [" + str(final_time) + "]  Time for execution" + function.END)

    # Converting negative private key to positive value
    private_key = function.signCheck(private_key, public_key, PHI)  

    # Back check before continuing
    with yaspin(text="Checking private key...", color="yellow") as spinner:
        start_time = time.time()
        if (private_key * public_key) % PHI != 1:
            print(function.RED + "\n\nFatal Error: Failed to generate valid private key!\n" + function.END)
            function.os._exit(0)
        end_time = time.time()
        final_time = end_time - start_time
        spinner.ok("✔ " + function.GREEN + "[Done]" + function.END)
        print(function.GRAY + "  [" + str(final_time) + "]  Time for execution" + function.END)

    # Outputing all vulues for user 
    print("\n")
    output = PrettyTable()
    output.field_names = ["OUTPUT TABLE", " "]
    output.add_row(["Factors of modulo (primes)",str(factors[0]) + ", " + str(factors[1])])
    output.add_row(["Euler's phi",PHI])
    output.add_row([function.BLUE + "Private key" + function.END, function.BLUE + str(private_key) + function.END])
    print (output)
    print(function.END + "\n")

    # Exit
    input("Press enter to exit...")
