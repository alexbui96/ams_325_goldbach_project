from matplotlib.pyplot import plot


def sieve(n):
    # Create a n-element True array
    prime_list_temp = [True for i in range(n+1)]
    
    # Create a empty prime list
    prime_list = []
    
    # 0 and 1 are not prime
    prime_list_temp[0] = False
    prime_list_temp[1] = False
    
    # Find an estimate square root of n
    for i in range(n):
        res = i*i
        if res > n:
            break
    # Assign False (not prime) for multiple of prime number
    for j in range(2, i):
        if prime_list_temp[j]:
            for m in range(j*j, n+1, j):
                prime_list_temp[m] = False
    
    # Create prime number list based on True value in prime_list_temp
    for k in range(n+1):
        if prime_list_temp[k]:
            prime_list.append(k)
            
    return prime_list


def goldbach_dict(n):
    # Create a prime list up to n
    prime_list = sieve(n)
    temp = []
    gb_dict = {}
    for i in range(4, n+1, 2):
        j = 0
        while prime_list[j] <= i/2:
            if (i - prime_list[j]) in prime_list:
                gb_dict[i] = gb_dict.get(i,temp) + [(prime_list[j],i-prime_list[j])]
            j +=  1
                    
    return gb_dict

def goldbach_partition_count(n):
    gb_dict = goldbach_dict(n)
    count_list =[]
    for i in range(4, n+1, 2):  
        count_list.append((i, len(gb_dict[i])))
    
    return count_list

def plot_mod_6(n):

    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow

    gb_dict = goldbach_dict(n)

    mod_0 = []
    mod_0_p = []
    mod_2 = []
    mod_2_p = []
    mod_4 = []
    mod_4_p = []

    plt.ion()

    def makeFig():
        plt.plot(mod_0, mod_0_p, 'r.')
        plt.plot(mod_2, mod_2_p, 'y.')
        plt.plot(mod_4, mod_4_p, 'b.')


    for i in range (4, n + 1, 2):
        temp = len(gb_dict[i])
        print(i,temp)
        
        if i%6 == 0:
            mod_0.append(i)
            mod_0_p.append(temp)
        elif i%6 == 2:
            mod_2.append(i)
            mod_2_p.append(temp)
        else:
            mod_4.append(i)
            mod_4_p.append(temp)
        
        drawnow(makeFig)
        plt.pause(.0001)

def main():
    n = int(input("Enter upper bound number: "))
    plot_mod_6(n)

if __name__ == '__main__':
    main()