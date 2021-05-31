"""
This App is using Benjamin Felix's simplified 5% rule to evaluate if you're better off renting or buying a property
https://www.pwlcapital.com/rent-or-own-your-home-5-rule/

"""

rentalProperty = float(input("Enter the monthly rent of the apartment :\n$"))
houseCost = float(input('Enter the total cost of the house you want to compare:\n$'))

#Formats to two decimal places
formatRentalProperty ="{:.2f}".format(rentalProperty)
formatHouseCost = "{:.2f}".format(houseCost)

#the calculation
finalHouse = ((houseCost * 0.05)/12)
finalRental =((rentalProperty * 12)/0.05)

#Formats to two decimal places
formatFinalHouse = "{:.2f}".format(finalHouse)
formatFinalRental = "{:.2f}".format(finalRental)

#Formatting
print('\n--------------\n')

print(f'The monthly rent of the apartment:${formatRentalProperty}')
print(f'The theoretical value of that apartment as if it were a home would be: ${formatFinalRental}')

print(f'The total cost of the house:${formatHouseCost}')
print(f'The theoretical rent of that house would be: ${formatFinalHouse} per month')
