# Write a function called count_primes() that requires a umeric argument only.
# This function will display all the numbers on the screen existing primes in the range from zero to that
# number included, and will return the number of prime numbers you found.
# Clarification, by convention 0 and 1 are not considered prime


def count_primes(a):
    for number in range (2, a+1):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:  
                print (number)  

print(count_primes(19))