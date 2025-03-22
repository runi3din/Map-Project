# Number of months for 10 years (10 years = 120 months)
n_10_years = 15 * 12

# Corrected compound interest formula for 10 years
A_10_years = 15000000 * (1 + 2.625 / 100) ** n_10_years + 5000000 * (((1 + 2.625 / 100) ** n_10_years - 1) / (2.625 / 100))
print(A_10_years)

