# declare the variables
max10 = 9875
max12 = 40125
max22 = 85525
max24 = 163300
max32 = 207350
max35 = 518400

tier10_tax = max10 * .1
tier12_tax = tier10_tax + ((max12 - max10) * .12)
tier22_tax = tier12_tax + ((max22 - max12) * .22)
tier24_tax = tier22_tax + ((max24 - max22) * .24)
tier32_tax = tier24_tax + ((max32 - max24) * .32)
tier35_tax = tier32_tax + ((max35 - max32) * .35)

# define user input
gross_inc = input("Enter your gross income from your W-2 for 2020: $")
# print(gross_inc)

num_dep = input("How many dependents are you claiming? ")
# print(num_dep)

# convert the input values to numbers
gross_inc_float = float(gross_inc)
num_dep_int = int(num_dep)

# calculate taxable income, converting to integer to drop cents
tax_income = int(gross_inc_float - 12200 - (2000 * num_dep_int))
if tax_income <= 0:
	print("Your taxable income is: $0")
else:
	print("Your taxable income is: $", tax_income)

# calculate tax due
if tax_income <= 0:
	tax_due = 0
elif tax_income <= max10:
	tax_due = tax_income * 0.1
elif tax_income <= max12:
	tax_due = tier10_tax + ((tax_income - max10) * .12)
elif tax_income <= max22:
	tax_due = tier12_tax + ((tax_income - max12) * .22)
elif tax_income <= max24:
	tax_due = tier22_tax + ((tax_income - max22) * .24)
elif tax_income <= max32:
	tax_due = tier24_tax + ((tax_income - max24) * .32)
elif tax_income <= max35:
	tax_due = tier32_tax + ((tax_income - max32) * .35)
elif tax_income > max35:
	tax_due = tier35_tax + ((tax_income - max35) * .37)

# convert tax_due to integer
tax_due_int = int(tax_due)

# print the result
print("You owe ${} in taxes".format(tax_due_int))
