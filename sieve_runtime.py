import time
import csv
import matplotlib.pyplot as plt
from sympy import isprime

def sieve(n):
    start = time.time()
    prime_list_temp = [True for i in range (n+1)]
    prime_list = []
    prime_list_temp[0] = False
    prime_list_temp[1] =False

    for est_sq in range(n):
        if est_sq*est_sq >= n:
            break
    
    for prime in range(2, est_sq):
        if prime_list_temp[prime]:
            # Assign False (not prime) for multiple of prime number
            for num in range(prime*prime, n+1, prime):
                prime_list_temp[num] = False
    
    for prime in range(n+1):
        if prime_list_temp[prime]:
            prime_list.append(prime)
            # print(prime)
    end = time.time()

    print("Elapsed time for sieve method: {}".format(end - start))
    return end - start

def prime(num):
    
    start = time.time()
    prime_list = []

    for n in range (2, num+1):
        if isprime(n):
            prime_list.append(n)
            # print(m)
    end = time.time()
    print("Elapsed time for sympy.isprime() function: {}".format(end - start))
    return end - start

def main():
    num_list = [i for i in range(1000,1000001, 1000)]
    sieve_list = []
    prime_list = []
    
    with open("sieve_run_time_comparision.csv", 'w', newline= '') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(['number', 'sieve', 'other_method'])

        for i in range(len(num_list)):
            n = num_list[i]
            print("Number:",n)
            time1 = sieve(n)
            time2 = prime(n)
            sieve_list.append(time1)
            prime_list.append(time2)

            w.writerow([n, time1, time2])
    
if __name__ == "__main__":
    main()
