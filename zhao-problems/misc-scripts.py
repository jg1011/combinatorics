import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln
from math import floor

def log_f(n, m, k):
    N = n * (n - 1) / 2  # Compute N directly as float
    log_N = np.log(N)
    log_m = np.log(m)
    
    # Logarithm of binomial coefficient using gammaln
    log_binom_N_m = gammaln(N + 1) - gammaln(m + 1) - gammaln(N - m + 1)
    
    # Compute log(f)
    log_f_value = log_binom_N_m + k * log_m + (-k + 1) * log_N
    return log_f_value

def plot_log_f_with_C(n, C_values):
    N = n * (n - 1) / 2  # Compute N as float
    m_values = np.arange(floor(N/10), floor(N/1.01), 10)
    ln_n = np.log(n)
    
    plt.figure(figsize=(10, 6))
    
    for C in C_values:
        log_f_values = []
        for m in m_values:
            # Compute k for each m
            k = C * (n ** 2) * ln_n / m
            # Compute log_f(n, m, k)
            value = log_f(n, m, k)
            log_f_values.append(value)
        # Convert to numpy array
        log_f_values = np.array(log_f_values)
        # Handle any infinities or NaNs
        log_f_values = np.nan_to_num(log_f_values, nan=np.nan, posinf=np.nan, neginf=np.nan)
        # Plot the values
        plt.plot(m_values, log_f_values, label=f'C = {C}')
    
    plt.xlabel('m')
    plt.ylabel('log(f(n, m, k))')
    plt.title(f'Plot of log(f(n, m, k)) for n = {n}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# User-defined parameters
n = 1000  # Fixed value of n; you can change this as needed
C_values = [100, 200, 300]  # List of C values to plot; modify as desired

# Call the plotting function
plot_log_f_with_C(n, C_values)
