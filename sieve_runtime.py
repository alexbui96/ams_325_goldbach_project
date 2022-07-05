# useful libraries
from cProfile import label
import time
import csv
import matplotlib.pyplot as plt
from sympy import isprime
from drawnow import drawnow

def sieve(n):
    # time when the program start
    start = time.time()
    
    #  # Create a n+1-element True array (tempurary prime list)
    prime_list_temp = [True for i in range (n+1)]
    
    # Create a empty prime list
    prime_list = []
    
    # 0 and 1 are not prime
    prime_list_temp[0] = False
    prime_list_temp[1] =False

    # Find an estimate square root of n
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
    #time when the prime end
    end = time.time()

    print("Elapsed time for sieve method: {}".format(end - start))
    
    # time that the program take to run
    return end - start

def sympy_isprime(num):
    
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
    
    lower = int(input("Enter lower boundary: "))
    upper = int(input("Enter upper boundary: "))
    step = int(input("Enter step: "))
    
    
    # list of n to run
    num_list = [i for i in range(lower,upper+1, step)]
    
    # empty list to store output
    n_list = []
    sieve_list = []
    isprime_list = []
    
    def makeFig():
        plt.plot(n_list, sieve_list , "r-", label = "Sieve method")
        plt.plot(n_list, isprime_list, "b-", label = "sympy.isprime()")
        plt.legend(loc = 'best')
        plt.xlabel("Numbers")
        plt.ylabel("Elapsed time (seconds)")
        plt.title("Elapsed time comparision between Sieve method and sympy.isprime() function")
        # Save the plot
        plt.savefig("elapsed_time_comparision.png")
            
    # Create and write output to csv file
    with open("sieve_run_time_comparision.csv", 'w', newline= '') as csvfile:
        w = csv.writer(csvfile)
        #header
        w.writerow(['number', 'sieve', 'other_method'])

        # run multiple n
        for i in range(len(num_list)):
            n = num_list[i]
            n_list.append(n)
            print("Number:",n)
            time1 = sieve(n)
            time2 = sympy_isprime(n)
            sieve_list.append(time1)
            isprime_list.append(time2)
            
            # To graph dynamically
            drawnow(makeFig)
            plt.pause(.0001)

            # add result to csv file
            w.writerow([n, time1, time2])
    # Keep the plot open   
    plt.show(block = True)
    
if __name__ == "__main__":
    main()
