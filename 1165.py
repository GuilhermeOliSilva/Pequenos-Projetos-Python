valueDonation = 0

while True:
    value = float(input())
    if value == -1:
        break
    valueDonation += value

valueDonationReal = valueDonation * 2.50
print(f"VC$ {valueDonation:.2f}")
print(f"R$ {valueDonationReal:.2f}")