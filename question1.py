### Assignment 1

import math


# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# sorting list of ages
sorted_ages = sorted(ages)
print("sorted ages list :", sorted_ages)
# finding min age from sorted ages list
min_age = min(sorted_ages)
print("min age : ", min_age)
# finding max age from sorted ages list
max_age = max(sorted_ages)
print("max age : ", max_age)

# Add the min age and the max age again to the list
sorted_ages.extend((min_age, max_age))
print("sorted ages after adding min and max age : ", sorted_ages)

# calculating Median of Ages
sorted_ages = sorted(sorted_ages)
len_ages = len(sorted_ages)

if len_ages % 2 == 0:
    # median calculation for list with even items
    median_age = (sorted_ages[int(len_ages/2)-1] + sorted_ages[int(len_ages/2)]) / 2
else:
    # median calculation for list with odd items
    median_age = sorted_ages[math.ceil(len_ages/2)]
print("Median Age : ", median_age)
# calculating Average of Ages
avg_age = sum(sorted_ages)/len(sorted_ages)
print("Average Age : ", avg_age)
# calculating Range of Ages
range_age = max_age - min_age
print("Range of Age : ", range_age)
