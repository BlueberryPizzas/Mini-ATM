import math

amount = int(input("What is the Number of Dollars(USD) you Want to Split? "))

# * can't have more than half of the total be 20s
# * val = amount / 2
val = amount

# * Twentys
val = val / 20
val = math.floor(val)

twentys = val

left_over = twentys * 20

val = amount - left_over
last_val = val

# * Tens
val = val / 10
val = math.floor(val)

tens = val

left_over = tens * 10

val = last_val - left_over
last_val = val

# * Fives
val = val / 5
val = math.floor(val)

fives = val

left_over = fives * 5

val = last_val - left_over
last_val = val

# * Ones
ones = val

# Print it
print("Twentys: " + str(twentys) + " Tens:" + str(tens) +  " Fives:" + str(fives) + " Ones:" + str(ones))
