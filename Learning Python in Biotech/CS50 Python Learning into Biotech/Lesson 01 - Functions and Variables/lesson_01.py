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
print(N)
