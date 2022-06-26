# Function to generate prime numbers list up to n using sieve method
from cProfile import label
from re import T
from numpy import block
from sympy import elliptic_f


def sieve(n, print_console = True):
    print("The prime numbers up to {}:".format(n))
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
    for prime in range(n+1):
        if prime_list_temp[prime]:
            prime_list.append(prime)
            # Print prime numbers to the console
            if print_console:
                print(prime)
    return prime_list

# Function to create a dictionary for Goldbach's conjecture
# The keys are even numbers up to n
# Their corresponding values are Goldbach pairs
def strong_goldbach_pair(n, print_console = True):
    
    print("The Goldbach's strong conjecture pairs up to {}:".format(n))
    # Create a prime list up to n
    prime_list = sieve(n, print_console = False)
    
    strong_gb_dict = {}
    for i in range(4, n+1, 2):
        j = 0
        while prime_list[j] <= i/2:
            if (i - prime_list[j]) in prime_list:
                strong_gb_dict[i] = strong_gb_dict.get(i,[]) + [(prime_list[j],i-prime_list[j])]
            j +=  1
        if print_console:
            print(i, strong_gb_dict[i])
                    
    return strong_gb_dict

def strong_goldbach_partition_count(n, print_console = True):
    print("The number of Goldbach's strong conjecture partitions up to {}:".format(n))
    prime_list = sieve(n, print_console = False)
    
    count_dict ={}
    for i in range (4, n + 1, 2):
        temp = 0
        j = 0
        while prime_list[j] <= i/2:
            if (i - prime_list[j]) in prime_list:
                count_dict[i] = count_dict.get(i, temp) + 1
            j += 1
        
        if print_console:
            print("{}: {} partitions".format(i, count_dict[i]))
    
    return count_dict

# Function to compute weak goldbach pairs and create a weak goldbach pairs dict
# The keys are odd number from 9

def weak_goldbach_pair(n, print_console = True):
    print("The Goldbach's weak conjecture pairs up to {}:".format(n))
    # Create a prime list up to n
    prime_list = sieve(n, print_console = False)
    # Remove 2 since 2 is even prime number
    prime_list.remove(2)
    
    # Create empty dict to store weak goldbach pairs
    weak_gb_dict = {}
    
    for num in range(9, n+1, 2):
        for num1 in prime_list:
            # Stop computing if the first number in pair greater than n/3
            if num1 > n/3:
                break
            
            for num2 in prime_list:
                    if num2 < num1:
                        continue
                    else:
                        num3 = num - num1 - num2
                        if num3 < num2:
                            continue
                        else:
                            if num3 in prime_list:
                                weak_gb_dict[num] = weak_gb_dict.get(num, []) + [(num1, num2, num3)]
                            continue
                
        if print_console:
            print(num, weak_gb_dict[num])
    
    return weak_gb_dict

def weak_goldbach_partition_count(n, print_console = True):
    print("The number of Goldbach's weak conjecture partitions up to {}:".format(n))
    # Create a prime list up to n
    prime_list = sieve(n, print_console = False)
    prime_list.remove(2)
    
    count_dict = {}
    
    for num in range(9, n+1, 2):
        for num1 in prime_list:
            if num1 > n/3:
                break
            
            for num2 in prime_list:
                    if num2 < num1:
                        continue
                    else:
                        num3 = num - num1 - num2
                        if num3 < num2:
                            continue
                        else:
                            if num3 in prime_list:
                                count_dict[num] = count_dict.get(num, 0) + 1
                            continue
                
        if print_console:
            print(num, count_dict[num])
     
    return count_dict

def plot_weak_gb(n):
    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow
    
    count_dict = weak_goldbach_partition_count(n)
    num = []
    par = []
    
    def makeFig():
        plt.plot(num, par, "+")
        plt.xlabel("Odd numbers")
        plt.ylabel("Number of partitions")
        plt.title("Goldbach's weak conjecture partitions")
        
    for i in range(9, n + 1, 2):
        num.append(i)
        par.append(count_dict[i])
        
        drawnow(makeFig)
        plt.pause(0.0001)
        
    plt.show(block = True)
    
def plot_strong_gb_mod_3(n):

    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow
    
    count_dict = strong_goldbach_partition_count(n)
    
    # prime_list = sieve(n)
    
    r_0 = []
    r_0_p = []
    r_1 = []
    r_1_p = []
    r_2 = []
    r_2_p = []

    plt.ion()

    # Function to plot Goldbach partitions for drawnow()
    def makeFig():
        plt.plot(r_0, r_0_p, 'r.', label = 'r 0')
        plt.plot(r_1, r_1_p, 'y.', label = 'r 1')
        plt.plot(r_2, r_2_p, 'b.', label = 'r 2')
        
        plt.legend(loc = 'best')
        plt.xlabel("Even numbers")
        plt.ylabel("Number of partitions")
        plt.title("Goldbach's strong conjecture partitions of residue class of 3 up to {}".format(n))
        
    for i in range (4, n + 1, 2):
        temp = count_dict[i]
        
        if i%3 == 0:
            r_0.append(i)
            r_0_p.append(temp)
        elif i%3 == 1:
            r_1.append(i)
            r_1_p.append(temp)
        else:
            r_2.append(i)
            r_2_p.append(temp)
        
        drawnow(makeFig)
        plt.pause(.0001)
        
    plt.show(block = True)
           
def main():

    while True:
        n = int(input("Note: For Goldbach's weak conjecture computing, an upper bound input number must be greater than or equal to 9\nEnter upper bound number(Enter -1 to quit): "))
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
        print("\nAvailable options:\n"
              +"\tCompute Prime lists (1)\n"
              +"\tCompute Goldbach's strong conjecture pairs (2)\n" 
              + "\tCompute Goldbach partitions (3)\n"
              + "\tCompute Goldbach's weak conjecture pairs (4)\n"
              + "\tCompute Goldbach's weak conjecture partitions (5)\n"
              + "\tPlot Goldbach's strong conjecture partitions (6)\n"
              + "\tPlot Goldbach's weak conjecture partitions (7)\n"
              + "\tQuit (-1)\n")
        
        case = int(input("Enter option: "))
        if case == -1:
            break
        elif case not in range (1,8):
            print("Invalid input option!")
        elif case in range(1,8):
            valid = True
            break
    
    def weak_gb_valid_run(n, func):
        try:
            if n < 9:
                raise ValueError  
            else:    
                func(n)
        except ValueError:
            print("Invalid input number! Please re-enter upper bound number and available computing option the program!")
            main()
        
    def run(case):
        if case == 1:
            sieve(n)
        elif case == 2:
            strong_goldbach_pair(n)
        elif case == 3:
            strong_goldbach_partition_count(n)
        elif case == 4:
            weak_gb_valid_run(n, weak_goldbach_pair)  
        elif case == 5:
            weak_gb_valid_run(n, weak_goldbach_partition_count)
        elif case == 6:
            plot_strong_gb_mod_3(n)
        elif case == 7:
            weak_gb_valid_run(n, plot_weak_gb)
            
    if valid:
        run(case)
        
if __name__ == "__main__":
    main()