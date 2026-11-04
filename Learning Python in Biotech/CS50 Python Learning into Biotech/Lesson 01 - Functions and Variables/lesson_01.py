# ==================================================
# LESSON 01: FUNCTIONS AND VARIABLES
# Learning Python through Biotechnology Applications
# ==================================================

# EXERCISE 1: BACTERIAL POPULATION GROWTH

# Biotechnology Concept:
# Bacterial cells reproduce by binary fission.
# Under ideal conditions, the population doubles
# with each generation.

# Objective:
# Calculate the bacterial population after a given
# number of generations.

# Mathematical Formula:
# N = N0 * 2**g

# Variables:
# N0 = Initial number of bacterial cells
# g  = Number of generations
# N  = Final number of bacterial cells


# ==================================================
# PYTHON PROGRAMME
# ==================================================
g = int(input("What's the number of generations? "))
N0 = int(input("What's the initial number of bacterial cells? "))
N = N0 * 2**g
print(f"Final number of bacterial cells: {N} cells")

# SAMPLE TEST
# Initial bacterial cells (N0) = 100
# Number of generations (g) = 3
# Expected output = 800 cells


# ==========================================
# EXERCISE 2: CULTURE MEDIA PREPARATION
# ==========================================

# Biotechnology Concept:
# Culture media provide nutrients for microbial growth.
# The amount of powder depends on the volume and concentration.

# Objective:
# Calculate the quantity of culture medium powder required.

# Formula:
# Powder required (g) = Volume (mL) * Concentration (g/L) / 1000

# ==================================================
# PYTHON PROGRAMME
# ================================================== 

V = float(input("whats the volume of medium? "))
C = float(input("whats the concentration of medium? "))
M = (V * C)/1000
print(f"The amount of medium powder required is {M:.2f}g.")

# SAMPLE TEST
# Volume (V) = 250 mL
# Concentration (C) = 25 g/L
# Expected output = 6.25 g


# ==========================================
# EXERCISE 3: DNA SEQUENCE GC CONTENT
# ==========================================

# Biotechnology Concept:
# DNA consists of four nitrogenous bases:
# Adenine (A), Thymine (T), Guanine (G) and Cytosine (C).

# Objective:
# Calculate the GC content percentage of DNA.

# Formula:
# GC content (%) = (G + C) / Total bases * 100

# ==================================================
# PYTHON PROGRAMME
# ==================================================

T = int(input("What is the total number of bases? "))
bases = int(input("What is the number of guanine/cytosine bases? "))
GC = (bases / T) * 100
print(f"GC content is {GC:.2f}%")

# SAMPLE TEST
# Total number of bases (T) = 20
# Guanine/Cytosine bases (G+C) = 10
# Expected output = 50.00%





















