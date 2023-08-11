#Acompany wants to give a bonus of 13% of the sales made by its employees for them, you have to design a program that asks each employee for their first and last name and the total, you have to round the bonus to 2 digits. print the following message;'Hello! first_name last_name, your total sales is total_sales and you will receive a bonus of bonus'
first_name=input("Hello,What is your first name? ")
last_name=input("What is your last name? ")
total_sales=int(input("what is your total sales? "))

operation=(total_sales * 13)/100
round= round(operation,2)
print(f"Hello! {first_name} {last_name}, your total sales is {total_sales} and you will receive a bonus of {round}")