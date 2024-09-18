# Constants
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Seconds in a year

# Inputs from the user
birth_rate = float(input("How many seconds between births? "))  # seconds between births
death_rate = float(input("How many seconds between deaths? "))  # seconds between deaths
immigrant_rate = float(input("How many seconds between immigrations? "))  # seconds between immigrants
current_population = int(input("What is the current population? "))  # current population
years = int(input("How many years in the future? "))  # years into the future

# Calculate number of births, deaths, and immigrants per year
births_per_year = SECONDS_IN_A_YEAR / birth_rate
deaths_per_year = SECONDS_IN_A_YEAR / death_rate
immigrants_per_year = SECONDS_IN_A_YEAR / immigrant_rate

# Calculate total population change per year
population_change_per_year = births_per_year + immigrants_per_year - deaths_per_year

# Calculate future population
future_population = current_population + (population_change_per_year * years)

# Output the expected population in the future and determine if population increased or decreased
future_population = int(future_population)
population_change = "increased" if future_population > current_population else "decreased"

print(f"The population in {years} years will be {future_population}")
print(f"The population {population_change}")
# Enter Code here
# Read the README - under files on left
# Delete these three lines before submitting
