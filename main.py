Total_bill = int(input("Please enter the total bill amount in dollars: "))
People = int(input("Please enter the number of people: "))
Percentage = int(input("Please enter the percentage of tip: "))

tip_amount = (Total_bill * (Percentage/100))
final_amount = "{:.2f}".format((Total_bill + tip_amount) / People)
#We are rounding off the final amount to 2 decimal places using {:.nf}.format, where n is the decimal places

print("The amount to be payed by each individual is "+ final_amount+".")