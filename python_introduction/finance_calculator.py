annual_interest_rate = 0.05
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income-total_monthly_expenses
annual_projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ", "$",monthly_savings)
print("Projected savings after one year, with interest, is :", "$",annual_projected_savings)