def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

# Exchange rates (as of today taking as example)
usd_to_pkr_rate = 277.00
eur_to_pkr_rate = 325.00
sar_to_pkr_rate = 74.25
dxb_to_pkr_rate = 28.50
inr_to_pkr_rate = 3.75

amount = float(input("Enter the amount: "))
choice_from = int(input("Select the currency to convert from:\n1. USD\n2. EUR\n3. SAR\n4. DXB\nEnter choice (1-4): "))

# Checking if the amount enterd is non-negative
if amount >= 0:
    
    if choice_from == 1:  # USD
        converted_amount = convert_currency(amount, usd_to_pkr_rate)
    elif choice_from == 2:  # EUR
        converted_amount = convert_currency(amount, eur_to_pkr_rate)
    elif choice_from == 3:  # SAR
        converted_amount = convert_currency(amount, sar_to_pkr_rate)
    elif choice_from == 4:  # DXB
        converted_amount = convert_currency(amount, dxb_to_pkr_rate)
    else:
        print("Invalid choice.")
        exit()

    
    choice_to = int(input("Select the currency to convert to:\n1. PKR\n2. INR\nEnter choice (1-2): "))
    
    if choice_to == 1:
        print(f"Converted amount: {converted_amount:.2f} PKR")
    elif choice_to == 2:
        inr_amount = convert_currency(converted_amount, inr_to_pkr_rate)
        print(f"Converted amount: {inr_amount:.2f} INR")
    else:
        print("Invalid choice.")
else:
    print("Invalid amount. Please enter a non-negative value.")
