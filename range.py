#for i in range(4):
#    print(i)


#print(list(range(0, 100, 2)))





# supplies = ['pens', 'flame-throwers', 'binders']
#
# for i in range(len(supplies)):
#     print('Index ' + str(i + 1) + ' in supplies is: ' + supplies[i])


# assignment

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]


# Multiple assignment trick
size, color, disposition = cat

print(size)

# swap values
a = 'AAA'
b = 'BBB'

a, b = b, a
print(a, b)
