week_1 = [10,15,22,31,24,14,17]
week_2 = [15,22,32,13,21,24]
last_day_sales= int (input("No. of lemonades sold on last day : "))
week_2.append(last_day_sales)
week_1.extend(week_2)
sales=week_1[:]
print("Earning on best day is : ", 1.5 * max(sales))
print("Sales on worst day is : ", 1.5 * min(sales))
print(sales * 1.5)
print(sum(sales)*1.5)
