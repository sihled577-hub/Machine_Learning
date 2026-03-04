#
# Sihle, 2026/3/3
# Sihle_for_3_data.py
# Use loop to calculate sum and use len to know the number of the element
#

# Accumulate a running total
sales_data = [12_000, 18_500, 9_300, 22_100, 15_600]
total = 0

for sale in sales_data:
    total += sale                        # way to say the total = total + sale

print(f"Total Sales: ${total:,}")        # a colon and a comma mean you print a colon after the third number
print(f"Average Sale: ${total / len(sales_data):,.2f}")   # the 2f is what is used to add decimal points .2f is two numbers after the decimal points

# len stands for the number of elements in the sales data range