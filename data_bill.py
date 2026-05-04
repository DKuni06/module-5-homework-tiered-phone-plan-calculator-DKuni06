# constant values are set here:
INCLUDED_DATA = 10
HIGH_DATA = 20
NORMAL_PRICE = 2
PREMIUM_PRICE = 1
NORMAL_HIGHPRICE = 3
PREMIUM_HIGHPRICE = 2
overage_data = 0
within_limit = "Default"

# Your code goes here:
data_used = int(input("Enter data used: "))
plan_cost = int(input("Enter your monthly plan cost: "))
is_premium = input("Do you have a premium plan? (yes or no): ")

if is_premium == "yes":
    if data_used > INCLUDED_DATA:
        overage_data = data_used - INCLUDED_DATA
        within_limit = "You are above your data limit."
        if data_used > HIGH_DATA:
            overage_cost = overage_data * PREMIUM_HIGHPRICE
        else:
            overage_cost = data_used * PREMIUM_PRICE
    else:
        within_limit = "You are within your data limit."
elif data_used > INCLUDED_DATA:
    overage_data = data_used - INCLUDED_DATA
    within_limit = "You are above your data limit."
    if data_used > HIGH_DATA:
        overage_cost = overage_data * NORMAL_HIGHPRICE
    else:
        overage_cost = data_used * NORMAL_PRICE
else:
    within_limit = "You are within your data limit."



total_bill = overage_cost + plan_cost
print(f"{within_limit}")
print(f"GB over limit: {overage_data} GB")
print(f"Overage cost: ${overage_cost}")
print(f"Total bill: ${total_bill}")