# a = list(input("Enter first list").split())
# b = list(input("Enter second list").split())
# if len(a)==len(b):
#     dictionary = list(zip(a,b))
#     print(sorted(dictionary))
# else:
#     print("Length Should Be Equal")



# a = list(input("List 1").split())
# b = list(input("List 2").split())
# dic = list(zip(a,b))
# key = input("Type a key")
# print("Value is",dic.get(key))




# deduction_standard = 150000
# deduction_80c = int(input("Enter your 80c-"))
# deduction_80cc = int(input("Enetr your 80cc-"))
# deduction_HRA = int(input("Enter your HRA-"))
# deduction_Medical = int(Input("Enter your MEdical-"))
# gross_income = int(input("Enter your Gross Income"))
# deduction_Total =deduction_standard + deduction_80c + deduction_80cc + deduction_HRA + deduction_Medical
# tax_income = (gross_income - deduction_Total)
# if(tax_income > 0):
# elif (gross_income<=500000):
#     income_tax = (tax_income*.1)
# elif (gross_income<=1000000) and (gross_income>500000):
#     income_tax = 25000 + ((gross_income-500000)*.2)
# elif (gross_income>1000000) and (gross_income<=100000) :
#     income_tax = 75000 +((gross_income-1000000)*3)
#     print("gross income is",gross_income)
#     print("Total deduction is ",deduction_Total)
#     print("Tax is",tax_income)
# else:
#     print("No Income Tax")



a = int(input("Enter a"))
b = int(input("enter b"))
for i in range (a,b):
    if (i%2 == 0):
        print(i)






