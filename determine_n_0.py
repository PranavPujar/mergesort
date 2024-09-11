from matplotlib import pyplot as plt
import numpy as np

input_sizes = [1, 10, 50, 100, 500, 1000, 2000]
execution_times = [0.000001, 0.0001, 0.0003, 0.001, 0.02, 0.05, 0.14]

poly_coefficients = np.polyfit(input_sizes, execution_times, 2)
predicted_times = np.polyval(poly_coefficients, input_sizes)

if __name__ == '__main__':
    plt.figure(figsize=(8, 6))
    plt.scatter(input_sizes, execution_times, color='blue', marker='o', label="Execution Times")
    plt.plot(input_sizes, predicted_times, linestyle='--', color='red', label="Quadratic Fit")
    # Mark the n_0 threshold 
    plt.axvline(x=100, color='purple', linestyle='--', label='Threshold n_0 ~ 100')  
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Time Complexity Analysis -- Zoomed in View')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 500)
    plt.ylim(0, 0.03)
    plt.show()
