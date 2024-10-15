from compound import interest_math
from prime_n import all_prime
from sum_any import sum_any_number
from letter_counter import count_letters

a = int(input("Press 1 for Compounding math:\nPress 2 for Finding Primes:\nPress 3 for Finding sum from 1 to n:\nPress 4 for Letter Counter:\n"))

if a == 1:
    pv = float(input("Enter the present value: "))
    year = float(input("How Many Years(n): "))
    interest = float(input("Enter the interest rate(%): "))
    
    result = interest_math(pv, year, interest)
    print(f"The amount that would be deposited at the end of {year} years is: {result}")
elif a == 2:
    n = int(input("Enter number for prime: "))
    primes = all_prime(n)
    print(f"All the prime numbers from 1 to {n} is: ")
    print(primes)

elif a == 3:
    n=int(input("Enter your number that you want to summarize: "))
    summation = sum_any_number(n)
    print(f"Summation from 1 to {n} is: {summation}")

elif a == 4:
    letter_count= input("Type or paste your text and hit enter: ")
    length = count_letters(letter_count)
    print(f"The letter count of your text is: {length}")

else:
    print("Invalid Number; Try again")