#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Morillas-Fourier Method (MFM) Supplementary Code

This script illustrates how to:
1. Generate a Fibonacci-based sequence: floor(F_n / n^1.5) + 2.
2. Apply a trigonometric (Fourier-like) correction to shift each base value to a prime.
3. Evaluate how the fraction of prime outputs depends on the number of correction coefficients (K).
4. Measure runtime for different K values and produce CSV and plots.

Dependencies:
  - numpy
  - sympy
  - mpmath
  - matplotlib
  - pandas

Usage Example:
  python MFM_Prime_Generation.py

Written for demonstration purposes; performance for large n might require further optimizations.
"""

import numpy as np
import sympy
import mpmath
import time
import pandas as pd
import matplotlib.pyplot as plt

# Configure mpmath precision for big Fibonacci computations if needed
mpmath.mp.dps = 50  # 50-digit precision

# ---------------------------
# PARAMETERS
# ---------------------------
N_MAX = 5000                  # Up to n=5000 for demonstration
K_VALUES = [5, 10, 15, 20]    # Different K values to test
FILENAME_RESULTS = "MFM_Prime_Analysis.csv"
FILENAME_TIME_PLOT = "Time_vs_K.png"
FILENAME_PRIME_PLOT = "Prime_Fraction_vs_K.png"

# ---------------------------
# HELPER FUNCTIONS
# ---------------------------

def fibonacci_sympy(n):
    """
    Returns the nth Fibonacci number using sympy's built-in arbitrary-precision integer method.
    This is safe for moderately large n (thousands), but can be slow for very large n.
    """
    return sympy.fibonacci(n)

def base_MFM(n):
    """
    Base formula: floor(F_n / n^1.5) + 2
    """
    # Avoid zero or negative n^1.5
    if n < 1:
        return 2  # fallback
    F_n = fibonacci_sympy(n)
    denominator = n**1.5
    return int((F_n // denominator) + 2)  # floor division approach

def correction_fourier(n_array, K):
    """
    Generates a 'Fourier-like' correction for demonstration.
    Here we simulate random coefficients in [-2,2] for each k < K.
    For each n, sum_{k=0}^{K-1} (coeffs[k] * cos(2*pi*k*n / N)).
    N is the length of the array.
    NOTE: This is a toy example. In an actual MFM approach, the coefficients
          would be computed to exactly align each value to a prime, typically via DCT inverse.
    """
    N = len(n_array)
    # Example: random "toy" coefficients for demonstration
    coeffs = np.random.uniform(-2, 2, K)
    # sum over k
    corrections = np.zeros(N, dtype=float)
    for k in range(K):
        freq = (2.0 * np.pi * k) / N
        corrections += coeffs[k] * np.cos(freq * n_array)
    # Rounding to nearest int so we can add it to the base integer values
    return np.round(corrections)

def is_prime_pythonic(x):
    """
    Simple prime check using sympy's isprime, which is typically fast for mid-range.
    """
    # x might be negative or zero if correction overshoot. We ensure positivity
    if x < 2:
        return False
    return sympy.isprime(x)

# ---------------------------
# MAIN SCRIPT
# ---------------------------
def main():
    # Store results in lists of (K, prime_count, prime_fraction, time_seconds)
    results = []
    times = []

    # We'll create an array of n values from 1..N_MAX
    n_values = np.arange(1, N_MAX + 1, dtype=int)

    for K in K_VALUES:
        start_time = time.time()

        # Step 1: build the base MFM array
        base_vals = [base_MFM(n) for n in n_values]

        # Step 2: build the correction array
        correction_vals = correction_fourier(n_values, K)

        # Step 3: combine base + correction
        # Some values might be negative if correction overshoots, but let's keep it for demonstration
        sequence_vals = [base_vals[i] + int(correction_vals[i]) for i in range(len(n_values))]

        # Step 4: check primality
        prime_flags = [is_prime_pythonic(val) for val in sequence_vals]
        prime_count = sum(prime_flags)
        prime_fraction = prime_count / float(len(sequence_vals))

        end_time = time.time()
        elapsed = end_time - start_time

        times.append(elapsed)
        results.append((K, prime_count, prime_fraction, elapsed))

        print(f"K={K}, prime_count={prime_count}, fraction={prime_fraction:.4f}, time={elapsed:.2f}s")

    # Convert results to DataFrame, save CSV
    df = pd.DataFrame(results, columns=["K", "Prime_Count", "Prime_Fraction", "Time_Sec"])
    df.to_csv(FILENAME_RESULTS, index=False)
    print(f"\nSaved analysis to {FILENAME_RESULTS}\n")

    # Plot Time vs K
    plt.figure(figsize=(8, 4))
    plt.plot(K_VALUES, times, marker='o', linestyle='-', color='blue')
    plt.xlabel("Number of Fourier Coefficients (K)")
    plt.ylabel("Computation Time (s)")
    plt.title("Computation Time vs. K")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(FILENAME_TIME_PLOT)
    print(f"Saved time plot to {FILENAME_TIME_PLOT}")

    # Plot Prime Fraction vs K
    plt.figure(figsize=(8, 4))
    plt.plot(K_VALUES, [r[2] for r in results], marker='s', linestyle='-', color='red')
    plt.xlabel("Number of Fourier Coefficients (K)")
    plt.ylabel("Fraction of Prime Outputs")
    plt.title("Prime Fraction vs. K")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(FILENAME_PRIME_PLOT)
    print(f"Saved prime fraction plot to {FILENAME_PRIME_PLOT}")

if __name__ == "__main__":
    main()