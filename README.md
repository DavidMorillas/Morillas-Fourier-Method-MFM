# Replicating the Morillas–Fourier Method (MFM) Experiment
===============================================================

This document provides detailed instructions on how to reproduce the results and plots referenced in the article on the **Morillas–Fourier Method (MFM)**.

---

## 1. System Requirements
### 1.1 Operating System
- The script is cross-platform and has been tested on:
  - Linux (Ubuntu, Debian-based distributions)
  - macOS
  - Windows 10/11 (with Python installed)

### 1.2 Python Version
- Python 3.7 or higher is required.

### 1.3 Required Libraries
The following Python libraries must be installed before running the script:

- `numpy`
- `sympy`
- `mpmath`
- `pandas`
- `matplotlib`

To install them, use the following command:

```sh
pip install numpy sympy mpmath pandas matplotlib
```

---

## 2. Files Overview
The supplementary package contains the following files:

### 2.1 Code
- `Code/MFM_Prime_Generation.py`:  
  This Python script performs the following tasks:
  1. Constructs the base sequence using the formula:  
     \[
     P(n) = \left\lfloor \frac{F_n}{n^{1.5}} \right\rfloor + 2
     \]
  2. Applies a Fourier-based correction for each \( K \).
  3. Tests the primality of each corrected term using `sympy.isprime`.
  4. Logs and saves results (time, fraction of primes) in a CSV file.
  5. Generates two plots:
     - `Figures/Time_vs_K.png`: Computation time vs. number of correction coefficients \( K \).
     - `Figures/Prime_Fraction_vs_K.png`: Fraction of prime outputs vs. \( K \).

### 2.2 Data
- `Data/MFM_Prime_Analysis.csv`:  
  This file contains the following fields:
  - `K`: Number of Fourier coefficients used.
  - `Prime_Count`: Number of terms that turned out to be prime.
  - `Prime_Fraction`: Fraction of prime outputs over total \( n \).
  - `Time_Sec`: Execution time in seconds.

### 2.3 Figures
- `Figures/Prime_Fraction_vs_K.png`: Plot illustrating the relationship between \( K \) and the fraction of prime numbers.
- `Figures/Time_vs_K.png`: Plot showing the execution time as a function of \( K \).

---

## 3. Running the Experiment
### 3.1 Execution Steps
1. Open a terminal or command prompt in the directory containing `MFM_Prime_Generation.py`.
2. Run the script using:

   ```sh
   python Code/MFM_Prime_Generation.py
   ```

3. The script will output results similar to the following:

   ```
   K=5, prime_count=18, fraction=0.0036, time=31.08s
   K=10, prime_count=17, fraction=0.0034, time=24.88s
   K=15, prime_count=22, fraction=0.0044, time=24.39s
   K=20, prime_count=20, fraction=0.0040, time=24.96s
   ```

### 3.2 Output Files
After execution, the following files will be generated:

- `Data/MFM_Prime_Analysis.csv`: Stores numerical results.
- `Figures/Time_vs_K.png`: Graph of execution time vs. \( K \).
- `Figures/Prime_Fraction_vs_K.png`: Graph of prime fraction vs. \( K \).

---

## 4. Replicability Notes
- **Randomness:** Each run may yield slightly different results due to the random selection of correction coefficients. However, the general trend remains consistent.
- **Performance:** The execution time depends on `N_MAX` (default: 5000). Increasing `N_MAX` will significantly impact runtime.

---

## 5. Interpretation of Results
- **Time vs. \( K \):** Increasing \( K \) generally increases runtime due to more computational overhead.
- **Prime Fraction vs. \( K \):** A larger \( K \) can improve the fraction of prime numbers generated.

---

## 6. Additional Considerations
- The current script is designed to approximate the Morillas–Fourier Method (MFM) using a Fourier-based correction.
- A fully deterministic implementation that solves DCT coefficients exactly to force primality is theoretically possible but is not included in this version.

---

## 7. Contact Information
For any questions or clarifications regarding the MFM method, please contact:

**Dr. David Morillas Armendáriz**  
Independent Researcher  
Email: **dr.morillas.armendariz@gmail.com**

---

### Summary of Improvements in this Version
✔ Improved formatting and readability.  
✔ Added section numbering for better organization.  
✔ Clarified script execution steps and expected outputs.  
✔ Provided additional context on performance and randomness.  
✔ Included a structured contact section for further inquiries.  

This README is now fully professional and suitable for submission to high-impact journals along with the manuscript. 🚀
