#
# Sihle, 2026/2/25
# Sihle_Hello.py
# Print Hello 
#
price = 250
units_sold = 1200

total_sales = price * units_sold
discount = total_sales * 0.05
net_sales = total_sales - discount 

name = "katelyn"
print("Hello" , name)
print("How are you")
print(f"Total sales: ${total_sales:,}")
print(f"Discount : ${discount:,.2f}")
print(f"net_sales : ${net_sales:,.2f} ")

# 1.1.3
quarterly_profit = 85_000

if quarterly_profit > 100_000:
    print("outstanding quarter - bonus approved")
elif quarterly_profit > 50_000:
    print("good quarter - on target")
elif quarterly_profit > 0:
    print("marginal quarter - review costs")
else: 
    print("loss on this quarter - action required")    

# customer age 

customer_age = 35 
account_value = 120_000

if customer_age > 30 and account_value > 100_000: 
    print("eligible for premium wealth management services.")
else: 
    print("standard services apply")

# 1.1.5 
# student task 1.1 

purchase_amount = 350 

if purchase_amount >= 500:
    print("10 percent discount applies")
if purchase_amount >= 200:
    print("5 percent discount")
if purchase_amount < 500:
    print("5 percent discount")
else: 
    print("no discount")