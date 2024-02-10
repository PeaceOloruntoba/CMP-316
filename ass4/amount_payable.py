def calculate_amount_payable(total_amount):
    if total_amount >= 100000:
        discount = 0.2 * total_amount
    elif 50000 <= total_amount < 100000:
        discount = 0.1 * total_amount
    elif 10000 <= total_amount < 50000:
        discount = 0.05 * total_amount
    else:
        discount = 0

    amount_payable = total_amount - discount
    return amount_payable

total_amount = float(input("Enter the total amount of goods: "))
result_amount = calculate_amount_payable(total_amount)
print(f"The amount payable after applying the discount is: {result_amount:.2f}")
