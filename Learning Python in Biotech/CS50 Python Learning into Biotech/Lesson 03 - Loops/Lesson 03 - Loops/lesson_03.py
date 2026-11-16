# ==================================================
# LESSON 03: LOOPS
# Learning Python through Biotechnology Applications
# ==================================================
# Concepts: while, for, range, break, continue, lists,
# len(), dictionaries, lists of dictionaries, nested loops,
# helper functions, and input screening.
#
# Educational examples only; not laboratory protocols.
# Run: python lesson_03.py
# ==================================================


# EXERCISE 1: BACTERIAL POPULATION GENERATIONS
# Concept: for loop and range()
# Formula: N = N0 * 2**g
# Sample: N0 = 100, generations = 3 -> 200, 400, 800
def exercise_01():
    N0 = int(input("Enter the initial bacterial population: "))
    generations = int(input("Enter the number of generations: "))
    population = N0

    for generation in range(1, generations + 1):
        population = population * 2
        print(f"Generation {generation}: {population} cells")


# EXERCISE 2: CULTURE MEDIA BATCH INPUT
# Concept: while loop, counter, continue, input screening
# Formula: Powder (g) = Volume (mL) * Concentration (g/L) / 1000
# Sample: 250 mL at 25 g/L -> 6.25 g

def exercise_02():
    batches = int(input("How many media batches? "))
    completed = 0

    while completed < batches:
        volume = float(input("Enter batch volume in mL: "))
        if volume <= 0:
            print("Volume must be greater than zero. Try again.")
            continue

        concentration = float(input("Enter concentration in g/L: "))
        if concentration <= 0:
            print("Concentration must be greater than zero. Try this batch again.")
            continue

        powder = volume * concentration / 1000
        completed = completed + 1
        print(f"Batch {completed}: {powder:.2f} g of powder required")


# EXERCISE 3: DNA NUCLEOTIDE COUNTER
# Concept: for loop and dictionary
# Sample: ATGCGCAT -> A=2, T=2, G=2, C=2
# Assumption: sequence contains only A, T, G and C.

def exercise_03():
    DNA = input("Enter a DNA sequence: ").upper()
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}

    for base in DNA:
        if base in counts:
            counts[base] = counts[base] + 1

    print(f"A: {counts['A']}")
    print(f"T: {counts['T']}")
    print(f"G: {counts['G']}")
    print(f"C: {counts['C']}")

# EXERCISE 4: DNA SEQUENCE LENGTH AND GC CONTENT
# Concept: len(), for loop, if
# Formula: GC content (%) = ((G + C) / total bases) * 100
# Sample: ATGCGCAT -> length 8; GC content 50.00%

def exercise_04():
    DNA = input("Enter a DNA sequence: ").upper()
    total_bases = len(DNA)

    if total_bases == 0:
        print("DNA sequence cannot be empty.")
        return

    GC_count = 0
    for base in DNA:
        if base == "G" or base == "C":
            GC_count = GC_count + 1

    GC_percentage = (GC_count / total_bases) * 100
    print(f"Total number of bases: {total_bases}")
    print(f"Number of G and C bases: {GC_count}")
    print(f"GC content: {GC_percentage:.2f}%")


# EXERCISE 5: LABORATORY SAMPLE LIST
# Concept: list, indexing, len(), range()
# Sample list: DNA001, DNA002, DNA003

def exercise_05():
    samples = ["DNA001", "DNA002", "DNA003", "DNA004"]
    print(f"Total samples: {len(samples)}")

    for index in range(len(samples)):
        print(f"Sample {index + 1}: {samples[index]}")


# EXERCISE 6: BIOTECH SAMPLE DICTIONARY
# Concept: dictionary keys, values, lookup, membership test

def exercise_06():
    samples = {
        "DNA001": "Blood",
        "DNA002": "Plant",
        "DNA003": "Bacterial culture",
        "DNA004": "Water"
    }

    for sample_id in samples:
        print(f"{sample_id}: {samples[sample_id]}")

    sample_id = input("Enter a sample ID to look up: ").upper()
    if sample_id in samples:
        print(f"Sample source: {samples[sample_id]}")
    else:
        print("Sample ID not found")

# Concept: helper function, list of dictionaries, len(), for loop
# Formula: Activity = product formed (micromoles) / time (minutes)
# Sample: 20 micromoles / 5 minutes = 4.00 micromoles/minute
# Simplified arithmetic example, not an assay protocol.

def calculate_activity(product, time):
    return product / time


def exercise_08():
    measurements = [
        {"product": 20, "time": 5},
        {"product": 30, "time": 6},
        {"product": 18, "time": 3}
    ]

    print(f"Number of measurements: {len(measurements)}")
    for index in range(len(measurements)):
        product = measurements[index]["product"]
        time = measurements[index]["time"]
        activity = calculate_activity(product, time)
        print(f"Measurement {index + 1}: {activity:.2f} micromoles/minute")


# EXERCISE 9: MICROTITER PLATE WELL MAP
# Concept: nested for loops
# A 96-well plate layout has 8 rows (A-H) and 12 columns (1-12).

def exercise_09():
    rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for row in rows:
        for column in range(1, 13):
            print(f"{row}{column}", end=" ")
        print()


# EXERCISE 10: COLONY GROWTH GRID
# Concept: nested loops and decomposition into helper functions
# Sample size = 3:
# * * *
# * * *
# * * *

def print_row(size):
    for _ in range(size):
        print("*", end=" ")
    print()


def print_grid(size):
    for _ in range(size):
        print_row(size)


def exercise_10():
    size = int(input("Enter the grid size: "))
    if size <= 0:
        print("Grid size must be positive.")
        return
    print_grid(size)


# MAIN MENU: run one exercise at a time

def main():
    while True:
        print("\n======================================")
        print("LESSON 03: LOOPS - BIOTECH EXERCISES")
        print("======================================")
        print("1. Bacterial Population Generations")
        print("2. Culture Media Batch Input")
        print("3. DNA Nucleotide Counter")
        print("4. DNA Length and GC Content")
        print("5. Laboratory Sample List")
        print("6. Biotech Sample Dictionary")
        print("7. Sample Records")
        print("8. Enzyme Activity Measurements")
        print("9. Microtiter Plate Well Map")
        print("10. Colony Growth Grid")
        print("0. Exit")

        choice = input("Choose an exercise (0-10): ")

        if choice == "1":
            exercise_01()
        elif choice == "2":
            exercise_02()
        elif choice == "3":
            exercise_03()
        elif choice == "4":
            exercise_04()
        elif choice == "5":
            exercise_05()
        elif choice == "6":
            exercise_06()
        elif choice == "7":
            exercise_07()
        elif choice == "8":
            exercise_08()
        elif choice == "9":
            exercise_09()
        elif choice == "10":
            exercise_10()
        elif choice == "0":
            print("Exiting Lesson 03. Keep practising!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 10.")


if __name__ == "__main__":
    main()
