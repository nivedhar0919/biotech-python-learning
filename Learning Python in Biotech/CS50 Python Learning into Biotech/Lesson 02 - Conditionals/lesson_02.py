# ==========================================
# LESSON 02: CONDITIONALS
# ==========================================

# Biotechnology Applications of CS50 Lecture 1
# Concepts: if, elif, else, Boolean expressions,
# comparison operators, logical operators, modulo,
# match/case


# ==================================================
# EXERCISE 1: BACTERIAL COLONY CLASSIFICATION
# ==================================================

# Biotechnology Concept:
# Bacterial colonies are visible groups of bacterial
# cells that grow on solid culture media.
# Colony counting is commonly used in microbiology
# to estimate the number of viable microorganisms.

# Objective:
# Classify the number of bacterial colonies observed
# as Low, Moderate, or High using conditional statements.

# Classification Criteria:
# Below 30 colonies       = Low colony count
# 30 to 100 colonies      = Moderate colony count
# Above 100 colonies     = High colony count

# Note:
# These are illustrative programming thresholds,
# not universal microbiological standards.

# Variables:
# colonies = Number of bacterial colonies observed


# ==================================================
# PYTHON PROGRAMME
# ==================================================

colonies = int(input("Enter the number of colonies observed: "))

if colonies < 30:
    print("Low colony count")
elif 30 <= colonies <= 100:
    print("Moderate colony count")
elif colonies > 100:
    print("High colony count")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Input: 15
# Expected output: Low colony count

# Test 2:
# Input: 30
# Expected output: Moderate colony count

# Test 3:
# Input: 75
# Expected output: Moderate colony count

# Test 4:
# Input: 100
# Expected output: Moderate colony count

# Test 5:
# Input: 150
# Expected output: High colony count



# ==================================================
# EXERCISE 2: pH-BASED SOLUTION CLASSIFICATION
# ==================================================

# Biotechnology Concept:
# pH is a measure of how acidic or alkaline a solution is.
# It is important in biotechnology because enzymes,
# microbial cultures, and biochemical reactions are
# influenced by the pH of their environment.

# Objective:
# Classify a solution based on its pH value as acidic,
# neutral, or basic using conditional statements.

# Classification Criteria:
# pH below 7       = Acidic
# pH equal to 7    = Neutral
# pH above 7       = Basic

# Variables:
# pH = Measured pH value of the solution


# ==================================================
# PYTHON PROGRAMME
# ==================================================

pH = float(input("Enter the pH value observed: "))

if 0 <= pH < 7:
    print("Acidic")
elif pH == 7:
    print("Neutral")
elif 7 < pH <= 14:
    print("Basic")
else:
    print("Incorrect pH value")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Input: 2.5
# Expected output: Acidic

# Test 2:
# Input: 6.8
# Expected output: Acidic

# Test 3:
# Input: 7.0
# Expected output: Neutral

# Test 4:
# Input: 7.5
# Expected output: Basic

# Test 5:
# Input: 8.5
# Expected output: Basic

# Test 6:
# Input: 12.0
# Expected output: Basic

# Test 7:
# Input: 15
# Expected output: Incorrect pH value



# ==================================================
# EXERCISE 3: DNA NUCLEOTIDE IDENTIFICATION
# ==================================================

# Biotechnology Concept:
# DNA contains four nitrogenous bases:
# Adenine (A), Thymine (T), Guanine (G), and Cytosine (C).
#
# Adenine and Guanine are classified as purines.
# Thymine and Cytosine are classified as pyrimidines.

# Objective:
# Identify whether an entered DNA nucleotide is a
# purine or a pyrimidine using match-case statements.

# Classification Criteria:
# A or G = Purine
# C or T = Pyrimidine
# Any other character = Invalid nucleotide

# Variables:
# Nucleotide = Single DNA nucleotide entered by the user


# ==================================================
# PYTHON PROGRAMME
# ==================================================

Nucleotide = input("Enter a single DNA nucleotide: ").upper()

match Nucleotide:
    case "A" | "G":
        print("Purine")
    case "C" | "T":
        print("Pyrimidine")
    case _:
        print("Invalid nucleotide")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Input: A
# Expected output: Purine

# Test 2:
# Input: G
# Expected output: Purine

# Test 3:
# Input: C
# Expected output: Pyrimidine

# Test 4:
# Input: T
# Expected output: Pyrimidine

# Test 5:
# Input: g
# Expected output: Purine

# Test 6:
# Input: X
# Expected output: Invalid nucleotide



# ==================================================
# EXERCISE 4: HAEMOGLOBIN LEVEL CLASSIFICATION
# ==================================================

# Biotechnology Concept:
# Haemoglobin is an iron-containing protein present in
# red blood cells. It transports oxygen throughout the body.
#
# Haemoglobin measurements are commonly expressed in g/dL.

# Objective:
# Classify a haemoglobin measurement as Low,
# Within Exercise Range, or High using conditional statements.

# Classification Criteria:
# Below 12.0 g/dL       = Low
# 12.0 to 16.0 g/dL     = Within exercise range
# Above 16.0 g/dL       = High

# Note:
# These are simplified programming thresholds for this
# exercise, not clinical reference ranges. Actual ranges
# vary depending on individual and laboratory factors.

# Variables:
# haemoglobin = Haemoglobin level entered by the user (g/dL)


# ==================================================
# PYTHON PROGRAMME
# ==================================================

haemoglobin = float(input("Enter a haemoglobin level in g/dL: "))

if haemoglobin < 12.0:
    print("Low")
elif 12.0 <= haemoglobin <= 16.0:
    print("Within exercise range")
else:
    print("High")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Input: 10.5
# Expected output: Low

# Test 2:
# Input: 12.0
# Expected output: Within exercise range

# Test 3:
# Input: 14.5
# Expected output: Within exercise range

# Test 4:
# Input: 16.0
# Expected output: Within exercise range

# Test 5:
# Input: 17.2
# Expected output: High



# ==================================================
# EXERCISE 5: PCR REACTION SUITABILITY CHECKER
# ==================================================

# Biotechnology Concept:
# PCR (Polymerase Chain Reaction) is a technique used
# to amplify a specific DNA sequence.
#
# A PCR reaction requires suitable conditions, including
# an appropriate reaction temperature, DNA template,
# and DNA polymerase.

# Objective:
# Determine whether a PCR reaction is suitable to proceed
# based on temperature, DNA template availability,
# and DNA polymerase availability.

# Suitability Criteria:
# Temperature between 50°C and 65°C = Suitable
# DNA template available            = Yes
# DNA polymerase available          = Yes
#
# All three conditions must be satisfied for the
# PCR reaction to be classified as suitable.

# Note:
# These are illustrative programming conditions, not
# a validated PCR protocol. Actual PCR conditions depend
# on the assay and reagents.

# Variables:
# Temperature     = Reaction temperature in °C
# DNA_template    = Availability of DNA template
# DNA_polymerase  = Availability of DNA polymerase


# ==================================================
# PYTHON PROGRAMME
# ==================================================

Temperature = float(input("Enter the reaction temperature: "))

DNA_template = input("Is the DNA template available? ").lower()

DNA_polymerase = input("Is DNA polymerase available? ").lower()

if 50 <= Temperature <= 65 and DNA_template == "yes" and DNA_polymerase == "yes":
    print("PCR reaction suitable")
else:
    print("PCR reaction not suitable")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Temperature: 60
# DNA template: yes
# DNA polymerase: yes
# Expected output: PCR reaction suitable

# Test 2:
# Temperature: 45
# DNA template: yes
# DNA polymerase: yes
# Expected output: PCR reaction not suitable

# Test 3:
# Temperature: 60
# DNA template: no
# DNA polymerase: yes
# Expected output: PCR reaction not suitable

# Test 4:
# Temperature: 60
# DNA template: yes
# DNA polymerase: no
# Expected output: PCR reaction not suitable

# Test 5:
# Temperature: 65
# DNA template: yes
# DNA polymerase: yes
# Expected output: PCR reaction suitable



# ==================================================
# EXERCISE 6: DNA SAMPLE QUALITY SCREENING
# ==================================================

# Biotechnology Concept:
# DNA sample quality is important before performing
# experiments such as PCR, DNA sequencing, and
# molecular cloning.
#
# DNA quality can be assessed using concentration,
# purity ratio (A260/A280), and contamination status.

# Objective:
# Determine whether a DNA sample is suitable for
# further molecular biology experiments based on
# concentration, purity, and contamination status.

# Quality Screening Criteria:
# DNA concentration >= 20 ng/uL = Suitable
# A260/A280 ratio between 1.8 and 2.0 = Suitable
# Contamination status = No
#
# All three quality requirements must be satisfied
# for the DNA sample to be classified as suitable.

# Note:
# These are illustrative programming criteria for
# learning Python, not universal laboratory standards.
# Actual acceptance criteria depend on the experiment
# and laboratory protocol.

# Variables:
# DNA_concentration = DNA concentration in ng/uL
# Purity_ratio       = A260/A280 purity ratio
# Contamination      = Whether the sample is contaminated


# ==================================================
# PYTHON PROGRAMME
# ==================================================

DNA_concentration = float(input("Enter DNA concentration (ng/uL): "))

Purity_ratio = float(input("Enter A260/A280 purity ratio: "))

Contamination = input("Is the DNA sample contaminated? ").lower()

if DNA_concentration >= 20 and 1.8 <= Purity_ratio <= 2.0 and Contamination == "no":
    print("DNA sample suitable")
else:
    print("DNA sample not suitable")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# DNA concentration: 50
# Purity ratio: 1.9
# Contamination: no
# Expected output: DNA sample suitable

# Test 2:
# DNA concentration: 15
# Purity ratio: 1.9
# Contamination: no
# Expected output: DNA sample not suitable

# Test 3:
# DNA concentration: 50
# Purity ratio: 1.5
# Contamination: no
# Expected output: DNA sample not suitable

# Test 4:
# DNA concentration: 50
# Purity ratio: 1.9
# Contamination: yes
# Expected output: DNA sample not suitable

# Test 5:
# DNA concentration: 20
# Purity ratio: 1.8
# Contamination: no
# Expected output: DNA sample suitable



# ==================================================
# EXERCISE 7: BACTERIAL GROWTH PHASE IDENTIFIER
# ==================================================

# Biotechnology Concept:
# Bacterial growth in a closed culture system is
# commonly described using four phases:
#
# 1. Lag phase:
#    Bacteria adapt to the new environment.
#
# 2. Log phase:
#    Bacteria multiply rapidly.
#
# 3. Stationary phase:
#    Cell growth and cell death rates are approximately
#    balanced.
#
# 4. Death phase:
#    The viable bacterial population decreases.

# Objective:
# Classify bacterial growth based on the given growth
# percentage using conditional statements.

# Classification Criteria:
# Below 10%              = Lag phase
# 10% to 100%            = Log phase
# Above 100% to 150%     = Stationary phase
# Above 150%             = Death phase

# Note:
# These are simplified programming thresholds for
# practising Python conditionals.
# Actual bacterial growth phases are identified using
# population measurements over time, not a single
# growth percentage.

# Variables:
# Growth_percentage = Bacterial growth percentage


# ==================================================
# PYTHON PROGRAMME
# ==================================================

Growth_percentage = float(input("Enter bacterial growth percentage: "))

if Growth_percentage < 10:
    print("Lag phase")
elif 10 <= Growth_percentage <= 100:
    print("Log phase")
elif 100 < Growth_percentage <= 150:
    print("Stationary phase")
else:
    print("Death phase")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Input: 5
# Expected output: Lag phase

# Test 2:
# Input: 10
# Expected output: Log phase

# Test 3:
# Input: 75
# Expected output: Log phase

# Test 4:
# Input: 120
# Expected output: Stationary phase

# Test 5:
# Input: 150
# Expected output: Stationary phase

# Test 6:
# Input: 180
# Expected output: Death phase



# ==================================================
# EXERCISE 8: LABORATORY SAMPLE BATCH IDENTIFIER
# ==================================================

# Biotechnology Concept:
# Biotechnology laboratories organise samples into
# batches for identification, tracking, and quality control.
#
# Numerical sample IDs can be classified as even or odd
# using the modulo operator.

# Objective:
# Identify whether a laboratory sample ID is even or odd.
# Also check whether the entered sample ID is valid.

# Classification Criteria:
# Sample ID <= 0       = Invalid sample ID
# Positive and even    = Even batch
# Positive and odd     = Odd batch

# Mathematical Concept:
# Sample_ID % 2 == 0 means the sample ID is even.
# Sample_ID % 2 != 0 means the sample ID is odd.

# Variables:
# Sample_ID = Numerical identification number of the sample


# ==================================================
# PYTHON PROGRAMME
# ==================================================

Sample_ID = int(input("Enter the Sample_ID: "))

if Sample_ID <= 0:
    print("Invalid sample ID")
elif Sample_ID % 2 == 0:
    print("Even batch")
else:
    print("Odd batch")


# ==================================================
# SAMPLE TESTS
# ==================================================

# Test 1:
# Input: 102
# Expected output: Even batch

# Test 2:
# Input: 105
# Expected output: Odd batch

# Test 3:
# Input: 200
# Expected output: Even batch

# Test 4:
# Input: 0
# Expected output: Invalid sample ID

# Test 5:
# Input: -15
# Expected output: Invalid sample ID


# ==================================================
# END OF LESSON 02: EXERCISES 08
# ==================================================




