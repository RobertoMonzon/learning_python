# Create a function called usd_to_eur that takes as its only parameter a numeric value (an amount in US dollars), and returns the equivalent amount in euros as its result. For the purposes of this example, we will take the conversion 1 USD = 0.90 EUR.

# Create a variable called dollars and store any amount in it to pass to your function and evaluate its result.

def usd_to_eur(dollar):
    euro=dollar*0.9
    return euro


print(f"{usd_to_eur(2)}")