# RSA
**Penetration of RSA cryptosystem with public keys factorization.**

RSA project is made under Brno University of Technology as study on mathematical principles of RSA cryptosystems. Goal of this project is to try develop best possible and most resource efficient algorithm for getting private key from public elements (*modulo, public key*). Obviously we don't expect penetration of bigger keys than let's say 64 bit. This program is made only for education purposes. 

## Functions of program

Here is what our program can do (so far 😉)

 1.  **Factorization of modulo (w/ size under 56 bit) to prime numbers**
 - Program takes input from user, which is composed of modulo and public key.  
 - Divide modulo to 3 parts *middle, beginning* and *ending*  
 - We    suppose, that primes which modulo is made of would be approximately    the same size, so first we try brute force attack on the *middle* part,    if we don't find any prime here than we test remaining parts.

 2.  **Compute private key** 
 - When we get both secret primes from modulo we can easily compute *Euler's PHI*.
 - Than we input that value w/ *public key* to the *Extended Euclidean Algorithm*, which finds inversion for *public key*. That inversion is our ***private key***.  
 - After that we can decrypt anything encrypted with public key.
 
 **Other functions**
 - Showing execution time of factorization and private key computing
 - Prime number list generation (but veeeery slow)
 - Check if number is prime number (even slower)

## What we are working on

**Multiprocess factorization**
We are trying to achieve more optimal usage of computing power with using all cores of processor we are executing our tests on.
**Exeptions**
Try to take care of all exceptions and error states, program can get in. 

## Contributions

Our team can not accept direct contribution to this repository, but we will be very happy to receive any other help. Thank you. ❤
