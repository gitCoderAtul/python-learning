days = ('mon','tue','wed','thu','wed')
 
day1= list(days)
print(day1)

day2= []
for values in day1:
    print(values)
    if values not in day2:
        day2.append(values)

print(day2)
day3 = tuple(day2)
print(day3)