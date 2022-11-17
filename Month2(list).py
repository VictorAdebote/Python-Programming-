#creating a list
function=[8,True,8.5,'Victor','olly',4.8,False,2,6.3,9]
# Acessing elementsin a list
print(function[2])
print(function[4])
print(function[9])
# Applying methods to elements in a list
print(function[4].upper())
print(function[3].lower())
# List slicing
print(function[0:6])
print(function[7:9])
print(function[4:10])
# Adding elements to a list
function.append('Luminous')
function.insert(7,'Formal')
function.extend(['Joy','Love'])
print(function)
# Remove elements from/items from a list
del function[11:13]
print(function)
del function[3:8]
function.remove(8)
print(function)
print(function.pop(0))
print(function)
print(function.pop(4))
print(function)