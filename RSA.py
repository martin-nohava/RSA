import time
from yaspin import yaspin
from prettytable import PrettyTable
from functions import *
import multiprocessing

print("""
   ____  ____    _    
  |  _ \/ ___|  / \   
  | |_) \___ \ / _ \  
  |  _ < ___) / ___ \ 
 .|_| \_\____/_/   \_\.
--public key cracking--                    
                     """)

#vkládané parametry
print("---enter parametrs---")
public_key = int(input("Enter public key: "))
modulo = int(input("Enter modulo: "))
input("-press enter to begin-")
print("\n")

#zjistime r, s
with yaspin(text="Finding primes...", color="yellow") as spinner:
    factors, factorization_time = factorization_switch(modulo)
    spinner.ok("✔ \033[0;32m[Done]\033[0;0m")
    print("\033[1;30m  [" + str(factorization_time) + "]  Time for execution\033[0;0m")

#zjistime PHI
PHI = (factors[0]-1) * (factors[1]-1)
    
#zjistim private_key w/ euclid
with yaspin(text="Finding private key...", color="yellow") as spinner:
    start_time = time.time()
    not_inversion, private_key = extendedEuclidianAlgirithmInversion(PHI, public_key)
    end_time = time.time()
    inversion_time = end_time - start_time
    spinner.ok("✔ \033[0;32m[Done]\033[0;0m")
    print("\033[1;30m  [" + str(inversion_time) + "]  Time for execution\033[0;0m")

#oprava znamenka
private_key = signCheck(private_key, public_key, PHI)    

#output log
print("\n")
output = PrettyTable()
output.field_names = ["OUTPUT TABLE", " "]
output.add_row(["Factors of modulo (primes)",str(factors[0]) + ", " + str(factors[1])])
output.add_row(["Euler's phi",PHI])
output.add_row(["\033[;33mPrivate key\033[0;0m","\033[;33m" + str(private_key) + "\033[0;0m"])
print (output)
print("\033[0;0m\n")

input("Press enter to exit...")
