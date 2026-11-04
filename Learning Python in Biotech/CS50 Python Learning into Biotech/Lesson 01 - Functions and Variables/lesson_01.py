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


# ==========================================
# EXERCISE 4: ADVANCED DNA GC CONTENT
# ==========================================

# Biotechnology Concept:
# GC content represents the percentage of
# Guanine (G) and Cytosine (C) in DNA.

# Objective:
# Calculate GC content directly from a DNA sequence.

# Formula:
# GC (%) = (G + C) / Total bases * 100

# ==================================================
# PYTHON PROGRAMME
# ==================================================
DNA = input("Enter the DNA sequence: ").upper()
G = DNA.count("G")
C = DNA.count("C")
T = len(DNA)
GC = ((G + C)/T)*100
print(f"Total number of bases: {T}")
print(f"Number of G bases: {C}")
print(f"Number of C bases: {C}")
print(f"Total GC content is {GC:.2f}%")

# SAMPLE TEST
# DNA sequence = ATGCGCAT
# Total bases = 8
# G bases = 2
# C bases = 2
# Expected output = 50.00%

# ==========================================
# EXERCISE 5: PROTEIN MOLECULAR WEIGHT
# ==========================================

# Biotechnology Concept:
# Proteins are made up of amino acid residues.
# Average amino acid residue mass = 110 Da.

# Objective:
# Estimate the molecular weight of a protein.

# Formula:
# Molecular weight (Da) = Number of residues * 110

# ==================================================
# PYTHON PROGRAMME
# ==================================================

Residues = int(input("Enter the number of residues: "))
Molecular_weight = Residues*110
print(f"Molecular weight of the protein is {Molecular_weight} Da") 

# SAMPLE TEST
# Number of amino acid residues = 100
# Average residue mass = 110 Da
# Expected output = 11000 Da


# ==========================================
# EXERCISE 6: ENZYME ACTIVITY CALCULATOR
# ==========================================

# Biotechnology Concept:
# Enzymes accelerate biochemical reactions.

# Objective:
# Calculate enzyme activity.

# Formula:
# Enzyme activity (U) = Product formed (µmol) / Time (min)

# ==================================================
# PYTHON PROGRAMME
# ==================================================

Product_formed = float(input("Enter the product formed: "))
Time = float(input("Enter time taken: "))
U = (Product_formed)/Time
print(f"Enzyme activity is {U:.2f} U") 

# SAMPLE TEST
# Product formed = 12.5 µmol
# Time taken = 2.5 min
# Expected output = 5.00 U


# ==========================================
# EXERCISE 7: SOLUTION DILUTION CALCULATOR
# ==========================================

# Biotechnology Concept:
# Dilution reduces the concentration of a solution.

# Objective:
# Calculate the final concentration after dilution.

# Formula:
# C1 * V1 = C2 * V2
# C2 = (C1 * V1) / V2

# ==================================================
# PYTHON PROGRAMME
# ==================================================

C_1 = float(input("Enter the initial concentration: "))
V_1 = float(input("Enter the initial volume: "))
V_2 = float(input("Enter the final volume: "))
# C_1 * V_1 = C_2 * V_2
C_2 = (C_1 * V_2)/V_1
print(f"Final concentration is {C_2:.2f} mg/mL") 

# SAMPLE TEST
# Initial concentration = 10 mg/mL
# Initial volume = 100 mL
# Final volume = 200 mL
# Expected output = 5.00 mg/mL


# ==========================================
# EXERCISE 8: MICROBIAL GROWTH RATE
# ==========================================

# Biotechnology Concept:
# Microbial growth refers to an increase in the
# number of microbial cells over time.

# Objective:
# Calculate the average increase in bacterial
# population per unit of time.

# Formula:
# Growth rate = (Final population - Initial population) / Time

# ==================================================
# PYTHON PROGRAMME
# ==================================================

N_0 = float(input("Enter the initial bacterial population: "))
N = float(input("Enter the final bacterial population: "))
t = float(input("Enter the time taken: "))
G_R = (N-N_0)/t
print(f"Growth rate is {G_R:.2f} cells/hour") 

# SAMPLE TEST
# Initial population (N0) = 200 cells
# Final population (N) = 800 cells
# Time taken (t) = 3 hours
# Expected output = 200.00 cells/hour


# ==========================================
# EXERCISE 9: DNA GC CONTENT CALCULATOR
# ==========================================

# Biotechnology Concept:
# GC content represents the percentage of G and C bases in DNA.

# Objective:
# Calculate the GC content of a DNA sequence.

# Formula:
# GC% = ((G + C) / Total bases) * 100

# ==================================================
# PYTHON PROGRAMME
# ==================================================

def main():
    DNA = input("Enter the DNA sequence: ").upper()
    G = DNA.count("G")
    C = DNA.count("C")
    T = len(DNA)
    GC = calculate_gc(G, C, T)
    print(f"Total number of bases: {T}")
    print(f"Number of G bases: {G}")
    print(f"Number of C bases: {C}")
    print(f"Total GC content is {GC:.2f}%")
def calculate_gc(G, C, T):
    GC = ((G + C) / T) * 100
    return GC
main()

# SAMPLE TEST
# Input: ATGCGCAT
# Expected output:
# Total number of bases: 8
# Number of G bases: 2
# Number of C bases: 2
# Total GC content is 50.00%


# ==========================================
# EXERCISE 10: DNA SEQUENCE LENGTH CALCULATOR
# ==========================================

# Biotechnology Concept:
# DNA consists of nucleotide bases: A, T, G and C.

# Objective:
# Calculate the total number of bases in a DNA sequence.

# Formula:
# DNA length = Number of nucleotides

# ==================================================
# PYTHON PROGRAMME
# ==================================================

def main():
 DNA = input("Enter the DNA sequence: ").upper()
 DNA_Length = calculate_DNA(DNA)
 print(f"The DNA sequence length is {DNA_Length}")
def calculate_DNA(DNA):
  DNA_Length = len(DNA)
  return DNA_Length
main()

# SAMPLE TEST
# Input: ATGCGCAT
# Expected output: Total number of bases: 8


# ==========================================
# EXERCISE 11: PROTEIN MOLECULAR WEIGHT CALCULATOR
# ==========================================

# Biotechnology Concept:
# Proteins are made up of amino acid residues.

# Objective:
# Estimate the molecular weight of a protein.

# Formula:
# Molecular weight = Number of residues * 110

# ==================================================
# PYTHON PROGRAMME
# ==================================================

def main():
 Residues = int(input("Enter the number of amino acid residues: "))
 Molecular_weight = calculate_wt(Residues)
 print(f"The molecular weight of protein is {Molecular_weight} Da")
def calculate_wt(Residues):
 Molecular_weight = Residues * 110
 return Molecular_weight
main()

# SAMPLE TEST
# Input: 100
# Expected output:
# Approximate molecular weight: 11000 Da




















