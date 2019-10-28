from functions import isPrime, factorization, inversion

#vkládané parametry
public_key = int(input("Enter public key: "))
modulo = int(input("Enter modulo: "))

#zjistime r, s
factors = factorization(modulo)
print("Factors: r=" + str(factors[0]) + " s=" + str(factors[1]))

#zjistime PHI
PHI = (factors[0]-1) * (factors[1]-1)

#zjistim private_key
print("Private key value is: " + str(inversion(public_key, PHI)))

input("Press any key to exit...")
