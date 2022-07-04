# Function to generate prime numbers list up to n using sieve method
def sieve(n, print_console = True):

    # Print title
    if print_console:
        print("The prime numbers up to {}:".format(n))

    # Create a n-element True array (tempurary prime list)
    prime_list_temp = [True for i in range(n+1)]
    
    # Create a empty prime list
    prime_list = []
    
    # 0 and 1 are not prime
    prime_list_temp[0] = False
    prime_list_temp[1] = False
    
    # Find an estimate square root of n
    for est_sq in range(n):
        if est_sq*est_sq >= n:
            break
        
    # Assign True for primes and False for composites
    for prime in range(2, est_sq):
        if prime_list_temp[prime]:
            # Assign False (not prime) for multiple of prime number
            for num in range(prime*prime, n+1, prime):
                prime_list_temp[num] = False
    
    # Create prime number list based on True value in prime_list_temp
    for prime in range(n+1):
        if prime_list_temp[prime]:
            prime_list.append(prime)
            # Print prime numbers to the console
            if print_console:
                print(prime)
    return prime_list

# Function to save goldbach's strong and weak partitions count dict to csv
def to_csv(file_name, headers, dict):

    # Import library
    import csv

    # Create a new or override the existing csv file
    with open(file_name + ".csv", 'w', newline= '') as file:
        w = csv.writer(file)
        # Add headers
        w.writerow(headers)
        # Write csv file
        for num in dict.keys():
            w.writerow([num, dict[num]])    

# Function to create a dictionary for Goldbach's conjecture
# The keys are even numbers up to n
# Their corresponding values are Goldbach's strong conjecture pairs
def strong_goldbach_pair(n, print_console = True):

    # Print title
    if print_console:
        print("The Goldbach's strong conjecture pairs up to {}:".format(n))
    
    # Create a prime list up to n
    prime_list = sieve(n, print_console = False)
    
    # Empty dict to store Goldbach's strong conjecture pairs
    strong_gb_dict = {}
    
    # Check even numbers from 4 to n
    for num in range(4, n+1, 2):
        j = 0
        while prime_list[j] <= num/2:
            if (num - prime_list[j]) in prime_list:
                strong_gb_dict[num] = strong_gb_dict.get(num,[]) + [(prime_list[j],num-prime_list[j])]
            j +=  1
        
        # exit and report Goldbach fail
        if len(strong_gb_dict[num]) == 0:
            print("{} has no partition.".format(num))
            break
         
        # Print result to console
        if print_console:
            print(num, strong_gb_dict[num])
                    
    return strong_gb_dict

# Function to count the number of Goldbach partitions for each even numbers
# The keys are even numbers up to n
# The values are the number of partitions of each even number
def strong_goldbach_partition_count(n, print_console = True, save_csv = True):

    # Print title
    if print_console:
        print("The number of Goldbach's strong conjecture partitions up to {}:".format(n))

    # Compute the prime list
    prime_list = sieve(n, print_console = False)
    
    # Empty dict to store outputs
    count_dict ={}

    # Check even numbers up to n
    for num in range (4, n + 1, 2):
        j = 0
        # Check the first prime number in the pair up to n/2
        while prime_list[j] <= num/2:
            if (num - prime_list[j]) in prime_list:
                # Count 1 if the other number is prime
                count_dict[num] = count_dict.get(num, 0) + 1
            j += 1
            
        # exit and report Goldbach fail
        if count_dict[num] == 0:
            print("{} has no partition.".format(num))
            break
        
        # Print result to console
        if print_console:
            print("{}: {} partitions".format(num, count_dict[num]))

    # Save outputs to csv    
    if save_csv:
        to_csv("strong_goldbach_partition_count_up_to_{}".format(n), ['Even number', 'Number of partitions'], count_dict)
                
    return count_dict

# Function to compute weak goldbach pairs and create a weak goldbach pairs dict
# The keys are odd number from 9
# Their corresponding values are Goldbach's weak conjecture pairs
def weak_goldbach_pair(n, print_console = True):
    
    # Print title
    if print_console:
        print("The Goldbach's weak conjecture pairs up to {}:".format(n))

    # Create a prime list up to n
    prime_list = sieve(n, print_console = False)
    # Remove 2 since 2 is even prime number
    prime_list.remove(2)
    
    # Empty dict to store weak goldbach pairs
    weak_gb_dict = {}
    # Check odd numbers from 9 up to n
    for num in range(9, n+1, 2):
        for num1 in prime_list:
            # Stop computing if the first number in the pair greater than n/3
            if num1 > n/3:
                break
            for num2 in prime_list:
                    # The second number in the pair must be greater than or equal to the first number
                    if num2 < num1:
                        continue
                    else:
                        # Compute the last number in a pair
                        num3 = num - num1 - num2
                        # The third number in the pair must be greater than or equal to the second number
                        if num3 < num2:
                            continue
                        else:
                            # Check if the third number is prime
                            if num3 in prime_list:
                                # Add the pair to dict
                                weak_gb_dict[num] = weak_gb_dict.get(num, []) + [(num1, num2, num3)]
                            continue
        # exit and report Goldbach fail
        if len(weak_gb_dict[num]) == 0:
            print("{} has no partition.".format(num))
            break
        
        # Print result to console        
        if print_console:
            print(num, weak_gb_dict[num])
    
    return weak_gb_dict

# Function to count the number of Goldbach partitions for each odd numbers
# The keys are odd numbers up to n
# The values are the number of partitions of each odd number
def weak_goldbach_partition_count(n, print_console = True, save_csv = True):

    # Print title
    if print_console:
        print("The number of Goldbach's weak conjecture partitions up to {}:".format(n))

    # Create a prime list up to n
    prime_list = sieve(n, print_console = False)
    # Remove prime number 2
    prime_list.remove(2)
    
    # Empty dict to store output
    count_dict = {}
    
    for num in range(9, n+1, 2):
        # pair = (num1, num2, num3) with num1 <=  num2 <= num3
        # First prime number in pair
        for num1 in prime_list:
            # stop loop
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
        
        # exit and report Goldbach fail
        if count_dict[num] == 0:
            print("{} has no partition.".format(num))
            break
        
        # Print result to console        
        if print_console:
            print("{}: {} partitions".format(num, count_dict[num]))
    
    # Save the output to csv
    if save_csv:
        to_csv("weak_goldbach_partition_count_up_to_{}".format(n), ['Odd number', 'Number of partitions'], count_dict)
     
    return count_dict

# Function to plot the number of Goldbach's weak conjecture partitions agains their corresponding odd numbers
def plot_weak_gb(n, save_plot = True):
    
    # Import necessary libraries
    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow
    
    # Compute the number of Goldbach's weak conjecture partitions before plotting
    count_dict = weak_goldbach_partition_count(n, save_csv = False)
    
    # Empty list to store odd numbers and their corresponding Goldbach's weak conjecture partitions  
    num = []
    par = []
    
    # Function to plot Goldbach's weak conjecture partitions
    def makeFig():
        plt.plot(num, par, "+")
        plt.xlabel("Odd numbers")
        plt.ylabel("Number of partitions")
        plt.title("Goldbach's weak conjecture partitions up to {}".format(n))
        # Save the plot
        if save_plot:
            plt.savefig("gb_weak_conjecture_{}.png".format(n))
    
    # Store computed values    
    for i in range(9, n + 1, 2):
        num.append(i)
        par.append(count_dict[i])
        
        # To plot dynamically
        drawnow(makeFig)
        plt.pause(0.0001)
    
    # Keep the plot open    
    plt.show(block = True)
   
# Function to plot the number of Goldbach's strong conjecture partitions agains their corresponding even numbers in residue classes of 3
def plot_strong_gb_mod_3(n, save_plot = True):
    
    # Import necessary libraries
    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow
    
    # Compute the number of Goldbach's strong conjecture partitions before plotting
    count_dict = strong_goldbach_partition_count(n, save_csv = False)
    
    # Empty list to store multiple residue classes of 3
    r_0 = []
    r_0_p = []
    r_1 = []
    r_1_p = []
    r_2 = []
    r_2_p = []
    # Enable interactive mode.
    plt.ion()

    # Function to plot Goldbach's strong conjecture partitions
    def makeFig():
        
        # Plot different residue classes of 3 in different colors
        plt.plot(r_0, r_0_p, 'r.', label = '0 mod 3')
        plt.plot(r_1, r_1_p, 'y.', label = '1 mod 3')
        plt.plot(r_2, r_2_p, 'b.', label = '2 mod 3')
        
        # Labels of the plot
        plt.legend(loc = 'best')
        plt.xlabel("Even numbers")
        plt.ylabel("Number of partitions")
        plt.title("Goldbach's strong conjecture partitions of multiple residue classes of 3 up to {}".format(n))
        # Save the plot
        if save_plot:
            plt.savefig("gb_strong_conjecture_mod_3_{}.png".format(n))
        
    # Store computed values    
    for num in range (4, n + 1, 2):
        
        temp = count_dict[num]
        
        if num%3 == 0:
            r_0.append(num)
            r_0_p.append(temp)
        elif num%3 == 1:
            r_1.append(num)
            r_1_p.append(temp)
        else:
            r_2.append(num)
            r_2_p.append(temp)
          
        # To graph dynamically
        drawnow(makeFig)
        plt.pause(.0001)
    
    # Keep the plot open   
    plt.show(block = True)
    
# Function to plot the number of Goldbach's strong conjecture partitions agains their corresponding even numbers in residue classes of 3
def plot_strong_gb_mul_7(n, save_plot = True):
    
    # Import necessary libraries
    import matplotlib.pyplot as plt
    import pandas as pd
    from drawnow import drawnow
    
    # Compute the number of Goldbach's strong conjecture partitions before plotting
    count_dict = strong_goldbach_partition_count(n, save_csv = False)
    
    # Empty list to store different multiplication classes
    m_3 = []
    m_3_p = []
    m_5 = []
    m_5_p = []
    m_7 = []
    m_7_p = []
    m_35 = []
    m_35_p = []
    m_37 = []
    m_37_p = []
    m_57 = []
    m_57_p = []
    m_357 = []
    m_357_p = []
    
    # Enable interactive mode.
    plt.ion()

    # Function to plot Goldbach's strong conjecture partitions
    def makeFig():
        
        # Plot different multiplication class in different colors
        plt.plot(m_3, m_3_p, 'g.', label = 'Multiplication of 3')
        plt.plot(m_5, m_5_p, 'r.', label = 'Multiplication of 5')
        plt.plot(m_7, m_7_p, 'b.', label = 'Multiplication of 7')
        plt.plot(m_35, m_35_p, 'y.', label = 'Multiplication of 3 and 5')
        plt.plot(m_37, m_37_p, 'c.', label = 'Multiplication of 3 and 7')
        plt.plot(m_57, m_57_p, 'm.', label = 'Multiplication of 5 and 7')
        plt.plot(m_357, m_357_p, 'k.', label = 'Multiplication of 3, 5 and 7')
        
        # Labels of the plot
        plt.legend(loc = 'best')
        plt.xlabel("Even numbers")
        plt.ylabel("Number of partitions")
        plt.title("Goldbach's strong conjecture partitions in different multiplication classes up to {}".format(n))
        # Save the plot
        if save_plot:
            plt.savefig("gb_strong_conjecture_mulplication_{}.png".format(n))
        
    # Store computed values    
    for num in range (4, n + 1, 2):
        
        temp = count_dict[num]
        
        if (num%3 == 0) & (num%5 == 0) & (num%7 == 0):
            m_357.append(num)
            m_357_p.append(temp)
        elif (num%3 == 0) & (num%5 == 0) & (num%7 != 0):
            m_35.append(num)
            m_35_p.append(temp)
        elif (num%3 == 0) & (num%5 != 0) & (num%7 == 0):
            m_37.append(num)
            m_37_p.append(temp)
        elif (num%3 != 0) & (num%5 == 0) & (num%7 == 0):
            m_57.append(num)
            m_57_p.append(temp)
        elif (num%3 == 0) & (num%5 != 0) & (num%7 != 0):
            m_3.append(num)
            m_3_p.append(temp)
        elif (num%3 != 0) & (num%5 == 0) & (num%7 != 0):
            m_5.append(num)
            m_5_p.append(temp)
        elif (num%3 != 0) & (num%5 != 0) & (num%7 == 0):
            m_7.append(num)
            m_7_p.append(temp)     
          
        # To graph dynamically
        drawnow(makeFig)
        plt.pause(.0001)
    
    # Keep the plot open   
    plt.show(block = True)

# Function to check valid uppper bound number
def n_input(limit = 4):
    valid_n = False
    # To take and check valid input upper bound number
    # Run until valid input or exit the program
    while True:
            
        n = input("***Note:\n"
                  + "\tFor Goldbach's strong conjecture computing, an upper bound input number must be greater than or equal to 4.\n" 
                  + "\tFor Goldbach's weak conjecture computing, an upper bound input number must be greater than or equal to 9.\nEnter upper bound number(Enter -1 to quit): ")
        # To check valid upper bound number n; n must be greater than or equal to limit
        try:
            n = int(n)
            # input -1 to exit
            if n == -1:               
                break
            # default limit = 4 for general Goldbach computation, 9 for Goldbach's weak conjecture
            if n < limit:
                # error for invalid input
                raise ValueError
            else:
                # run for valid input
                valid_n = True
                # stop loop
                break
        except ValueError:
            # error message
            print("Invalid input number!")
    return n, valid_n

# Function to check valid input options    
def run_valid():
        n, valid_n = n_input()
        
        # Create condition check to run the program
        valid_run = False
        # Initial value to avoid bugs
        case = 0
        # To take and check valid input option
        while valid_n:
            
            # Print available options
            print("\nAvailable options:\n"
                + "\tCompute Prime lists (1)\n"
                + "\tCompute Goldbach's strong conjecture pairs (2)\n" 
                + "\tCompute Goldbach's strong conjecture partitions (3)\n"
                + "\tCompute Goldbach's weak conjecture pairs (4)\n"
                + "\tCompute Goldbach's weak conjecture partitions (5)\n"
                + "\tPlot Goldbach's strong conjecture partitions residue class of 3 (6)\n"
                +"\tPlot Goldbach's strong conjecture partitions in different multiplication classes (7)\n"
                + "\tPlot Goldbach's weak conjecture partitions (8)\n"
                + "\tQuit (-1)\n")
            
            # To take input option
            case = input("Enter option: ")
            # check numeric input
            try:
                case = int(case)
            except ValueError:
                print("Invalid input option!")
                continue
            
            # check valid upper bound number for Goldbach's weak conjecture computation
            while case in [4, 5, 8]:
                try:
                    # Valid upper bound number must be greater than or equal to 9
                    if n == -1:
                        break
                    elif n < 9:
                        # error when n < 9
                        raise ValueError
                    else:
                        # stop loop
                        break  
                except ValueError:
                    print("Invalid input number for case option: {}".format(case))
                    # Re-run the program when the input upper bound number is invalid
                    n, valid_n = n_input(limit = 9)
            
            # To stop the program
            if case == -1:
                break
            # To check valid input options 
            elif case not in range (1,9):
                print("Invalid input option!")
            elif case in range(1,9):
                valid_run = True
                break
        return n, valid_run, case
    
# Function to run analysis options
def run(n, valid_run, case):
    # To run the program based on input option    
    if valid_run:
        if case == 1:
            sieve(n)
        elif case == 2:
            strong_goldbach_pair(n)
        elif case == 3:
            strong_goldbach_partition_count(n)
        elif case == 4:
            weak_goldbach_pair(n)     
        elif case == 5:
            weak_goldbach_partition_count(n)
        elif case == 6:
            plot_strong_gb_mod_3(n)
        elif case == 7:
            plot_strong_gb_mul_7(n)
        elif case == 8:
            plot_weak_gb(n)     
                 
# Main function to run           
def main():
    # To take input of upper bound number and available options
    n, valid_run, case = run_valid()
    
    # Run and re-run the program 
    while valid_run:
        run(n, valid_run, case)
        re_run = input("Test different analysis with same bound n = {}? (y/n/any other keys to exit): ". format(n))
        
        # Different analysis with the same bound
        if re_run == "y":
            case = input("\nAvailable options:\n"
            + "\tCompute Prime lists (1)\n"
            + "\tCompute Goldbach's strong conjecture pairs (2)\n" 
            + "\tCompute Goldbach's strong conjecture partitions (3)\n"
            + "\tCompute Goldbach's weak conjecture pairs (4)\n"
            + "\tCompute Goldbach's weak conjecture partitions (5)\n"
            + "\tPlot Goldbach's strong conjecture partitions residue class of 3 (6)\n"
            +"\tPlot Goldbach's strong conjecture partitions in different multiplication classes (7)\n"
            + "\tPlot Goldbach's weak conjecture partitions (8)\n"
            + "\tQuit (-1)\n"
            + "Enter available option: ")
            
            # check valid input options
            try:
                case = int(case)
                # check bound number for weak conjecture computation
                if case in [4, 5, 8]:
                    if n < 9:
                        raise ValueError
            # exit for invalid bound number  
            except ValueError:
                print("Invalid input or the upper bound number is less than 9 for the Goldbach's weak conjecture computation! Please re-run the program!")
                break
            # exit
            if case == -1:
                break
            # run if valid
            elif case in range (1,9):
                continue
         
        # Different bound number with the same analysis  
        elif re_run == "n":
            re_run = input("Current upper bound is n = {}, test a different bound with same analysis option: {}? (y/any other keys to exit): ". format(n, case))
            if re_run == "y":
                
                if case in [4, 5, 8]:
                    # take and check bound number for weak conjecture analysis
                    n, valid_n = n_input(limit = 9)  
                else:
                    # take bound number for genaral analysis
                    n, valid_n = n_input()
                # run if valid                                                
                if valid_n:
                    continue
                # exit
                elif n == -1:
                    break
            # exit for other input   
            else: 
                break
        # exit for other input
        else:
            break
# to run
if __name__ == "__main__":
    main()