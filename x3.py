brands=['nike','fila','puma']
print(brands)
print(type(brands))

brands.append('allen soley')
print(brands)

brands.insert(1,'reebok')
print(brands)

print(brands[0])
print(brands[1])
print(brands[2])
print(brands[3])

print(brands[-1])

print("For in loop")

for val in brands:
    print(val)

print("While loop ")
print(len(brands))

i=0
while i<len(brands):
    print(i, brands[i])
    i+=1

nos = [10,20,15,40,50,60,70,80,90]
nos_1 = []

for values in nos:
    if values>=18:
        nos_1.append(values)

print(nos)
print(nos_1)

print(30 in nos)
print(20 in nos_1)
   