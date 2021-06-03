def twoDecimalPlacer(number):
	newNumber = '{:.2f}'.format(number)
	print('$'+newNumber)

print('Want to make a sound investment decision?')
print('\nWell,with this app you can!\n')
print('We will compare the unrecoverable costs of an apartment vs a house!\n')
print('Unrecoverable costs are costs you will never see back.\nFor apartments,thats the rent.\nFor houses,that the maintenance and property tax.')
print()
print('With this handy app,you can compare the rent of an apartment to the total price of a house to make your decision!')

print('\n-------------------------------\n')

costOfRentalProperty = float(input("Enter the monthly rent of the apartment :\n$"))
costOfHouse = float(input('Enter the total cost of the house you want to compare:\n$'))

unrecoverableCostOfHouse = ((costOfHouse * 0.05)/12)
unrecoverableCostOfRental =((costOfRentalProperty * 12)/0.05)

formatCostOfRentalProperty ="{:.2f}".format(costOfRentalProperty)
formatCostOfHouse = "{:.2f}".format(costOfHouse)


formatUnrecoverableCostOfHouse = "{:.2f}".format(unrecoverableCostOfHouse)
formatUnrecoverableCostOfRental = "{:.2f}".format(unrecoverableCostOfRental)

print('\n-------------------------------\n')
print('THE COST OF RENTING')
print(f'The monthly rent of the apartment you entered:${formatCostOfRentalProperty}')
print(f'The theoretical value of that apartment as if it were a home would be: ${formatUnrecoverableCostOfRental}')
print('\n-------------------------------\n')
print('THE COST OF OWNING')
print(f'The total cost of the house you entered:${formatCostOfHouse}')
print(f'The unrecoverable of that house would be: ${formatUnrecoverableCostOfHouse} per month') 
print('\n-------------------------------\n')

tenYearMortgage = (costOfHouse/120)
twentyYearMortgage =(costOfHouse/240)
thirtyYearMortgage = (costOfHouse/360)

formatTenYearMortgage = "{:.2f}".format(tenYearMortgage)
formatTwentyYearMortgage = "{:.2f}".format(twentyYearMortgage)
formatThirtyYearMortgage = "{:.2f}".format(thirtyYearMortgage)

print("MONTHLY MORTGAGE PAYMENT")
print(f'The 10 year mortgage payment per month: ${formatTenYearMortgage}')
print(f'The 20 year mortgage payment per month: ${formatTwentyYearMortgage}')
print(f'The 30 year mortgage payment per month: ${formatThirtyYearMortgage}')
print('\n-------------------------------\n')

tenYearMortgageAndHouse = (tenYearMortgage) + unrecoverableCostOfHouse
twentyYearMortgageAndHouse = (twentyYearMortgage) + unrecoverableCostOfHouse
thirtyYearMortgageAndHouse = (thirtyYearMortgage) + unrecoverableCostOfHouse

formatTenYearMortgageAndHouse = "{:.2f}".format(tenYearMortgageAndHouse )
formatTwentyYearMortgageAndHouse = "{:.2f}".format(twentyYearMortgageAndHouse)
formatThirtyYearMortgageAndHouse = "{:.2f}".format(thirtyYearMortgageAndHouse)
print("TOTAL MONTHLY PAYMENT")
print(f'The 10 year mortgage with the unrecoverable cost is: ${formatTenYearMortgageAndHouse} per month')
print(f'The 20 year mortgage with the unrecoverable cost is: ${formatTwentyYearMortgageAndHouse} per month')
print(f'The 30 year mortgage with the unrecoverable cost is: ${formatThirtyYearMortgageAndHouse} per month')


print('\n-------------------------------\n')

if costOfRentalProperty == unrecoverableCostOfHouse:
	print('The apartment and house are equal in unrecoverable costs')	
elif costOfRentalProperty < unrecoverableCostOfHouse:
	print('The APARTMENT is the BETTER DEAL in terms of unrecoverable costs!')	
else:
	print('The HOUSE is the BETTER DEAL in terms of unrecoverable costs!')

	
print('\n-------------------------------\n')
print('Keep in mind this recommendation is based ONLY on unrecoverable cost. It disregards a mortgage payment')
print('If you are considering mortgage as a unrecoverable cost please refer to the TOTAL MONTHLY PAYMENT section')

'''
To Add later
Interest rates for a more accurate mortgage for the 10,20,30 payments. To be safe, so whatever the interest is, say 3.67% just make it 4%
'''