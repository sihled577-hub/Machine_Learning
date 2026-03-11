# 
# Sihle, 2026/3/11
# Sihle_W3.py
# Practice Lists
# 

sales_regions = ["North", "South", "East", "West", "Central"]

# print("First region:", sales_regions[0])
# print("Last region:", sales_regions[-1])
# print("Regions 3-5", sales_regions[3:5])
# THE ELEMENT IN THE STARTING NUMBER IS INCLUDED, WHILE THE ELEMENT IN THE ENDING NUMBER IS NOT INCLUDED

# Sorting lists 
# scores = [88, 72, 95, 61, 84, 99, 77]
# scores_sorted = sorted(scores, reverse=False)    # reverse means descending 
# print("Ranked scores:", scores_sorted) # This means you print an output named "Ranked scores" and python will print the scores in descending order

# employees = [
 #   {"name": "Alice",   "dept": "Sales",   "salary": 72_000},
#   {"name": "Bob",     "dept": "Finance", "salary": 85_000},
#     {"name": "Carol",   "dept": "Sales",   "salary": 69_000},
#    {"name": "David",   "dept": "IT",      "salary": 92_000},
# ]

# Filter Sales department only 
# sales_team = [e for e in employees if e["dept"] == "Sales"]
# IT_team = [e for e in employees if e["dept"] == "IT"]
# avg_sales_salary_IT = sum(e["salary"] for e in IT_team) / len(IT_team)


# print(f"Average Sales Salary for IT department: ${avg_sales_salary_IT:,.2f}")

# 1.3.5 
customers = [
    {"name": "Apex Corp",    "region": "East",  "purchases": 34_000},
    {"name": "BlueSky LLC",  "region": "West",  "purchases": 87_500},
    {"name": "CoreTech",     "region": "East",  "purchases": 12_200},
    {"name": "Delta Group",  "region": "West",  "purchases": 56_000},
    {"name": "Edge Systems", "region": "East",  "purchases": 29_800},
]

# Filter for the East region

East_customers = [c for c in customers if c["region"] == "East"]
West_customers = [w for w in customers if w["region"] == "West"]

# for c in East_customers:
# print(f"East customers: {c["name"]} ${c["purchases"]:,.2f}")

total_purchases = sum(w["purchases"] for w in West_customers)

print(f"Total Purchases: ${total_purchases:,.2f}")

 # customer.append({"name": "Fusion Inc", "region": "North", "purchases": 44_000})

highest_purchase = max(customers, key=lambda c: c["purchases"])
print(f"Highest Purchase: {highest_purchase["name"]} ${highest_purchase["purchases"]:,.2f}")

# [x  for x in range(1, 10, 2)]