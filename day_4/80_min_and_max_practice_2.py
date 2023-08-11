#Calculate the difference between the maximum and minimum value in the following list of numbers, and store it in a variable called range:

#list_numbers = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

list_numbers = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

num_max= max(list_numbers)
num_min=min(list_numbers)

range=(num_max-num_min)
print(range)