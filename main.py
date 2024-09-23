# Programmers: Oreoluwa Adebusoye, Jose Carrillo
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/25/2024
# Lab Assignment: 1
# What program does: This program determines the expected population in the future for a country
# based on a current population amount given (1) how often someone is born (in seconds),
# (2) how often someone dies (in seconds), and (3) how often a new immigrant joins the country (in seconds).

# Constants
seconds_in_a_year = 365 * 24 * 60 * 60  # Seconds in a year

# Inputs from the user
birth_rate = float(input("How many seconds between births? "))  # seconds between births
death_rate = float(input("How many seconds between deaths? "))  # seconds between deaths
immigrant_rate = float(input("How many seconds between immigrations? "))  # seconds between immigrants entering
current_population = int(input("What is the current population? "))  # current population
years = int(input("How many years in the future? "))  # years into the future

# Calculate number of births, deaths, and immigrants per year
births_per_year = seconds_in_a_year / birth_rate
deaths_per_year = seconds_in_a_year / death_rate
immigrants_per_year = seconds_in_a_year / immigrant_rate

# Calculate total population change per year
population_change_per_year = births_per_year + immigrants_per_year - deaths_per_year

# Calculate future population
future_population = current_population + (population_change_per_year * years)

# Output the expected population in the future  determine if population increased or decreased
future_population = int(future_population)

# Determine if population increased or decreased
if future_population > current_population:
    population_change = "increased"
else:
    population_change = "decreased"

# Print the results
print("The population in" ,years, "years will be" ,future_population)
print("The population" ,population_change)

