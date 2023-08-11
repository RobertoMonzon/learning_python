# Create the zip with the translations of the numbers from 1 to 5 in Spanish,french, Portuguese and English 
#(in the same order), and convert the generated object into a list stored in the numbers variable:


nums_eng=["one","two","three","four","five"]
nums_spa=["uno","dos","tres","cuatro","cinco"]
nums_por=["um","dois","tres","quatro","cinco"]
nums_fre=["un","deux","trois","quatre","cinq"]
my_zip=(zip(nums_eng,nums_spa,nums_por,nums_fre))

for nums_eng,nums_spa,nums_por,nums_fre in my_zip:
    print(f"{nums_eng} in spanish is written {nums_spa}, in portuguese is written {nums_por} and in french is written {nums_fre}")