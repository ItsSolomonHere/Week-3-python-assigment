def calculate_discount(price, discount_percent):
    """
    Calculates the discounted price based on the given price and discount percentage.

    Args:
      price: The original price of the item (must be positive).
      discount_percent: The discount percentage (whole number, e.g., 10 for 10%).
    """
    # Validate inputs
    if price <= 0 or discount_percent < 0:
        print("Error: Price and discount percentage must be positive values.")
        return  

    if discount_percent >= 20:
        discount_decimal = discount_percent / 100  # Convert to decimal
        discount = discount_decimal * price
        new_price = price - discount
        print(f'The discount is {discount_percent}%, and the new price is Ksh{new_price:.2f}. Thanks for shopping with us.')
    else:
        print(f"The discount percentage of {discount_percent}% is too low. The original price is Ksh{price:.2f}. Thanks for shopping with us.")

# Get user input
try:
    price = float(input("Enter the price: Ksh"))
    discount_percentage = int(input("Enter the discount percentage: "))

    # Call the function
    calculate_discount(price, discount_percentage)

except ValueError:
    print("Error: Please enter a valid number for price and discount percentage.")
