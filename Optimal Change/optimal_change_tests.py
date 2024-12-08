from optimal_change import optimal_change

# Common cases
print(optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print(optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

# Edge cases
# Exact payment, no change needed
print(optimal_change(50.00, 50) == " No change due")

# Underpayment, insufficient funds
print(optimal_change(75.00, 50) == "Hey Guy, I need more money!")

# Special case: rounding issues or very small values
print(optimal_change(49.99, 50) == "The optimal change for an item that costs $49.99 with an amount paid of $50 is 1 penny.")

print(optimal_change(75, 175) == "The optimal change for an item that costs $75 with an amount paid of $175 is 1 $100 bill.")