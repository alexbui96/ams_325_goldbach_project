# Function to generate prime numbers list up to n using sieve method
from sympy import elliptic_f


def sieve(n):
    # Create a n-element True array (tempurary prime list)
    prime_list_temp = [True for i in range(n+1)]
    
    # Create a empty prime list
    prime_list = []
    
    # 0 and 1 are not prime
    prime_list_temp[0] = False
    prime_list_temp[1] = False
    
    # Find an estimate square root of n
    for i in range(n):
        res = i*i
        # stop when reach 
        if res > n:
            break
        
    # Assign True for primes and False for composites
    for j in range(2, i):
        if prime_list_temp[j]:
            # Assign False (not prime) for multiple of prime number
            for m in range(j*j, n+1, j):
                prime_list_temp[m] = False
    
    # Create prime number list based on True value in prime_list_temp
    for k in range(n+1):
        if prime_list_temp[k]:
            prime_list.append(k)
            
    return prime_list

# Function to create a dictionary for Goldbach's conjecture
# The keys are even numbers up to n
# Their corresponding values are Goldbach pairs
def strong_goldbach_dict(n):
    # Create a prime list up to n
    prime_list = sieve(n)
    strong_gb_dict = {}
    for i in range(4, n+1, 2):
        j = 0
        while prime_list[j] <= i/2:
            if (i - prime_list[j]) in prime_list:
                strong_gb_dict[i] = strong_gb_dict.get(i,[]) + [(prime_list[j],i-prime_list[j])]
            j +=  1
                    
    return strong_gb_dict

def goldbach_partition_count(n):
    gb_dict = strong_goldbach_dict(n)
    count_list =[]
    for i in range(4, n+1, 2):  
        count_list.append((i, len(gb_dict[i])))
    
    return count_list

def plot_strong_gb_mod_3(n):

    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow

    prime_list = sieve(n)

    mod_0 = []
    mod_0_p = []
    mod_1 = []
    mod_1_p = []
    mod_2 = []
    mod_2_p = []

    plt.ion()

    # Function to plot Goldbach partitions for drawnow()
    def makeFig():
        plt.plot(mod_0, mod_0_p, 'r.')
        plt.plot(mod_1, mod_1_p, 'y.')
        plt.plot(mod_2, mod_2_p, 'b.')

    for i in range (4, n + 1, 2):
        temp = 0
        j = 0
        while prime_list[j] <= i/2:
            if (i - prime_list[j]) in prime_list:
                temp += 1
            j += 1
        print(i,temp)
        
        if i%3 == 0:
            mod_0.append(i)
            mod_0_p.append(temp)
        elif i%3 == 1:
            mod_1.append(i)
            mod_1_p.append(temp)
        else:
            mod_2.append(i)
            mod_2_p.append(temp)
        
        drawnow(makeFig)
        plt.pause(.0001)
    
def main():
    
    n = 0
    while n != -1:
        n = int(input("Enter upper bound number(Enter -1 to quit): "))
        if n == -1:
            break
        try:
            if n < 4:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid input number!")
    
    valid = False
    while n >= 4:
        case = int(input("Enter option (Enter -1 to quit): "))
        if case == -1:
            break
        elif case not in range (1,5):
            print("Invalid input!")
        elif case in range(1,5):
            valid = True
            break
    
    def run(case):
        if case == 1:
            print(sieve(n))
        elif case == 2:
            print(strong_goldbach_dict)
        elif case == 3:
            print(goldbach_partition_count)
        elif case == 4:
            plot_strong_gb_mod_3(n)
            
    if valid:
        run(case)
        
if __name__ == "__main__":
    main()