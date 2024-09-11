from matplotlib import pyplot as plt
import time


# Function f(n) given 
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x

def populate_times(n_lst, times):
    for n in n_lst:
        start = time.time()
        f(n)
        end = time.time()
        
        # Calculate elapsed time
        total = end - start
        times.append(total)

def plot(n_lst, times):
    plt.plot(n_lst, times, marker='o')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity of given function f(n)')
    plt.grid(True)
    plt.show()

n_lst = [1, 10, 50, 100, 500, 1000, 2000]

times = []
populate_times(n_lst, times)
plot(n_lst, times)
