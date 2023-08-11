# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

# capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
# countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]


capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

for capitals,countries in zip(capitals,countries):
    print(f"The capital of {countries} is {capitals}")
