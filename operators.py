# Operators Assignment
# Name: Jayanth Katta
# Topic: Arithmetic and Assignment Operators

print("========== BASIC QUESTIONS ==========")

# 1. Rahul buys 4 notebooks, each costing Rs.50.
notebooks = 4
cost_per_notebook = 50
total_cost = notebooks * cost_per_notebook
print("1. Total cost:", total_cost)

# 2. Total marks in Math and Science.
math_marks = 85
science_marks = 90
total_marks = math_marks + science_marks
print("2. Total marks:", total_marks)

# 3. Remaining water in the tank.
water = 120
water_used = 35
remaining_water = water - water_used
print("3. Remaining water:", remaining_water, "liters")

# 4. Total number of plants.
rows = 18
plants_per_row = 25
total_plants = rows * plants_per_row
print("4. Total plants:", total_plants)

# 5. Pizza cost shared among 6 friends.
pizza_cost = 480
friends = 6
amount_per_friend = pizza_cost / friends
print("5. Each friend pays:", amount_per_friend)

# 6. Chocolates distributed equally using floor division.
chocolates = 53
students = 5
chocolates_each = chocolates // students
print("6. Chocolates each student receives:", chocolates_each)

# 7. Remaining unpacked apples.
apples = 95
box_capacity = 10
remaining_apples = apples % box_capacity
print("7. Remaining apples:", remaining_apples)

# 8. Square of 14.
number = 14
square = number ** 2
print("8. Square of 14:", square)

# 9. Total distance covered.
laps = 8
distance_per_lap = 400
total_distance = laps * distance_per_lap
print("9. Total distance:", total_distance, "meters")

# 10. Average speed.
distance = 360
time = 6
average_speed = distance / time
print("10. Average speed:", average_speed, "km/h")

# 11. Total pages read.
pages_per_day = 18
days = 7
total_pages = pages_per_day * days
print("11. Total pages read:", total_pages)

# 12. Students in each classroom.
total_students = 720
classrooms = 12
students_per_classroom = total_students / classrooms
print("12. Students per classroom:", students_per_classroom)

# 13. Final bill after discount.
shirts = 3
shirt_cost = 650
discount = 200
final_bill = shirts * shirt_cost - discount
print("13. Final bill:", final_bill)

# 14. Total income.
salary = 30000
bonus = 5000
total_income = salary + bonus
print("14. Total income:", total_income)

# 15. Total cricket runs.
runs_per_over = 12
overs = 5
total_runs = runs_per_over * overs
print("15. Total runs:", total_runs)

print("\n========== BASIC ASSIGNMENT OPERATORS ==========")

# 16. Wallet balance.
wallet = 1000
wallet += 250
print("16. Wallet balance:", wallet)

# 17. Library books.
books = 500
books += 75
print("17. Total books:", books)

# 18. Biscuit stock.
biscuits = 120
biscuits -= 35
print("18. Remaining biscuits:", biscuits)

# 19. Game score.
score = 15
score += 10
print("19. Updated score:", score)

# 20. Employee count multiplied by 5.
employees = 40
employees *= 5
print("20. Updated employee count:", employees)

# 21. Students divided into groups.
students = 180
students /= 6
print("21. Students in each group:", students)

# 22. Complete boxes using floor division assignment.
items = 500
items //= 12
print("22. Complete boxes:", items)

# 23. Remaining pencils using modulus assignment.
pencils = 68
pencils %= 6
print("23. Remaining pencils:", pencils)

# 24. Square using exponent assignment.
number = 5
number **= 2
print("24. Square:", number)

# 25. Battery percentage.
battery = 100
battery -= 28
print("25. Remaining battery:", battery, "%")

# 26. Health points.
health = 50
health += 20
print("26. Updated health:", health)

# 27. Savings balance doubles.
balance = 5000
balance *= 2
print("27. Updated balance:", balance)

# 28. Printer sheets.
sheets = 240
sheets -= 48
print("28. Remaining sheets:", sheets)

# 29. Attendance points.
attendance = 60
attendance += 15
print("29. Total attendance points:", attendance)

# 30. Company profit.
profit = 80000
profit += 20000
print("30. Updated profit:", profit)

print("\n========== MEDIUM ARITHMETIC QUESTIONS ==========")

# Q1. Online Shopping.
tshirts = 5
cost_per_tshirt = 450
shipping = 120
total_bill = tshirts * cost_per_tshirt + shipping
print("Q1. Total bill:", total_bill)

# Q2. Average marks.
marks = [78, 85, 91, 67, 89]
average_marks = sum(marks) / len(marks)
print("Q2. Average marks:", average_marks)

# Q3. Pizza Party.
total_slices = 8 * 6
friends = 9
slices_each = total_slices // friends
remaining_slices = total_slices % friends
print("Q3. Slices each:", slices_each)
print("    Remaining slices:", remaining_slices)

# Q4. Bike Mileage.
distance = 360
petrol = 12
mileage = distance / petrol
print("Q4. Mileage:", mileage, "km/liter")

# Q5. Salary Increment.
salary = 48000
increment = salary * 12 / 100
new_salary = salary + increment
print("Q5. Increment amount:", increment)
print("    New salary:", new_salary)

# Q6. Cricket Match.
runs = 245
matches = 6
average_runs = runs / matches
print("Q6. Average runs:", average_runs)

# Q7. Electricity Bill.
cost_per_unit = 8
units = 325
bill = cost_per_unit * units
print("Q7. Electricity bill:", bill)

# Q8. Classroom Arrangement.
students = 137
capacity = 30
full_classrooms = students // capacity
remaining_students = students % capacity
print("Q8. Completely filled classrooms:", full_classrooms)
print("    Students left:", remaining_students)

# Q9. Library Fine.
fine_per_day = 12
late_days = 9
total_fine = fine_per_day * late_days
print("Q9. Total fine:", total_fine)

# Q10. Festival Discount.
phone_cost = 35000
discount = phone_cost * 15 / 100
final_price = phone_cost - discount
print("Q10. Discount amount:", discount)
print("     Final price:", final_price)

# Q11. Water Tank.
water = 2500
daily_usage = 185
days = 7
remaining_water = water - daily_usage * days
print("Q11. Remaining water:", remaining_water, "liters")

# Q12. Bakery.
cookies = 145
box_capacity = 12
full_boxes = cookies // box_capacity
remaining_cookies = cookies % box_capacity
print("Q12. Full boxes:", full_boxes)
print("     Cookies left:", remaining_cookies)

# Q13. Distance Covered.
laps = 7
distance_per_lap = 425
distance_meters = laps * distance_per_lap
distance_km = distance_meters / 1000
print("Q13. Distance in meters:", distance_meters)
print("     Distance in kilometers:", distance_km)

print("\n========== MEDIUM ASSIGNMENT OPERATORS ==========")

# Q14. Bank Account.
balance = 15000
balance += 3500
print("Q14. Updated balance:", balance)

# Q15. ATM Withdrawal.
balance = 25000
balance -= 7500
print("Q15. Updated balance:", balance)

# Q16. Grocery Store.
rice_bags = 120
rice_bags += 35
print("Q16. Stock after arrival:", rice_bags)
rice_bags -= 42
print("     Stock after sales:", rice_bags)

# Q17. Game Points.
points = 850
points += 250
print("Q17. After earning points:", points)
points -= 180
print("     After losing points:", points)
points *= 2
print("     After doubling:", points)

# Q18. School Attendance.
attendance = 55
attendance -= 6
print("Q18. Today's attendance:", attendance)
attendance -= 2
print("     Tomorrow's attendance:", attendance)

# Q19. Water Bottle.
water = 2.0
water -= 0.4
print("Q19. After drinking:", water, "liters")
water += 1.2
print("     After filling:", water, "liters")

# Q20. Warehouse.
boxes = 500
boxes /= 5
print("Q20. Boxes per branch:", boxes)

# Q21. Mobile Data.
data = 6.0
data -= 1.5
print("Q21. After usage:", data, "GB")
data += 3
print("     After recharge:", data, "GB")

# Q22. Savings Goal.
savings = 12000
monthly_saving = 2500
savings += monthly_saving
savings += monthly_saving
savings += monthly_saving
savings += monthly_saving
print("Q22. Final savings:", savings)

# Q23. Company Shares.
shares = 80
shares += 25
print("Q23. After buying:", shares)
shares -= 18
print("     After selling:", shares)

# Q24. Fuel in Car.
fuel = 45
fuel -= 18
print("Q24. After trip:", fuel, "liters")
fuel += 22
print("     After refuelling:", fuel, "liters")

# Q25. Mobile Wallet.
wallet = 2000
wallet += 500
print("Q25. After adding Rs.500:", wallet)
wallet -= 650
print("     After spending Rs.650:", wallet)
wallet += 1200
print("     After cashback:", wallet)
wallet -= 450
print("     After recharge:", wallet)

print("\n========== CHALLENGE QUESTIONS ==========")

# Q26. Movie Ticket Booking.
wallet = 2000
ticket_cost = 180
tickets = 4
wallet -= ticket_cost * tickets
print("Q26. Balance after ticket payment:", wallet)
wallet += 100
print("     Balance after cashback:", wallet)

# Q27. Online Course.
wallet = 10000
course_cost = 7500
scholarship = course_cost * 20 / 100
amount_to_pay = course_cost - scholarship
wallet -= amount_to_pay
print("Q27. Scholarship amount:", scholarship)
print("     Amount paid:", amount_to_pay)
print("     Remaining wallet balance:", wallet)

# Q28. Restaurant Bill Split.
bill = 3850
discount = bill * 10 / 100
discounted_bill = bill - discount
friends = 5
each_person = discounted_bill / friends
print("Q28. Discount amount:", discount)
print("     Discounted bill:", discounted_bill)
print("     Each person's contribution:", each_person)

# Q29. Library Membership.
membership_fee = 1200
advance = 500
remaining_amount = membership_fee
remaining_amount -= advance
print("Q29. Remaining amount:", remaining_amount)

# Q30. E-commerce Wallet.
wallet = 5000
wallet -= 1850
print("Q30. After buying headphones:", wallet)
wallet += 300
print("     After cashback:", wallet)
wallet -= 750
print("     After buying mouse:", wallet)
wallet += 2000
print("     Final wallet balance:", wallet)
